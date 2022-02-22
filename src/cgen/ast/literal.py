import enum
import struct

from .abstract import AbstractNode
from .utils import ValuedNodeMixin, NodeContext


class PrimitiveTypes(enum.Enum):
    Null = 0
    Bool = 1
    Int = 2
    Double = 3
    String = 4
    # aliases
    NULL = 0
    BOOLEANLITERAL = 1
    INTLITERAL = 2
    DOUBLELITERAL = 3
    STRINGLITERAL = 4

    bool = 1
    int = 2
    double = 3
    string = 4


class BaseLiteralNode(AbstractNode, ValuedNodeMixin):
    def __init__(self, ctx: NodeContext, value_type: str, value: str):
        super(BaseLiteralNode, self).__init__(ctx)
        self._value_type = BaseLiteralNode.get_type(value_type)
        self._literal_value = value

    def _run_scope_check(self):
        pass  # no checks needed

    def _run_type_check(self):
        pass  # no checks needed

    def generate_code(self):
        raise NotImplementedError

    @staticmethod
    def get_type(value_type: str) -> PrimitiveTypes:
        return PrimitiveTypes[value_type]

    def get_value(self):
        return self._literal_value


class StringLiteralNode(BaseLiteralNode):
    def generate_code(self):
        label = self.ctx.label_generator.get_label()
        self.ctx.data_segment += f'{label}:\t.asciiz\t{self._literal_value}\n'
        self.ctx.text_segment += f'\tla $v0, {label}\n'


class IntLiteralNode(BaseLiteralNode):
    def generate_code(self):
        self.ctx.text_segment += f'\tli $v0, {self._literal_value}\n'


class BoolLiteralNode(BaseLiteralNode):
    def generate_code(self):
        value = 1 if self._literal_value == 'true' else 0
        self.ctx.text_segment += f'\tli $v0, {value}\n'


class NullLiteralNode(BaseLiteralNode):
    def generate_code(self):
        self.ctx.text_segment += f'\tmove $v0, $zero\n'


class DoubleLiteralNode(BaseLiteralNode):
    def generate_code(self):
        label = self.ctx.label_generator.get_label()
        self.ctx.data_segment += f'{label}:\t.double\t{self._literal_value}\n'
        self.ctx.text_segment += f'\tl.d $f0, {label}\n'
