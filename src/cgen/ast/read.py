from .abstract import AbstractNode
from .literal import PrimitiveTypes
from .utils import ValuedNodeMixin, NodeContext


class ReadIntegerNode(AbstractNode, ValuedNodeMixin):
    def __init__(self, ctx: NodeContext):
        super(ReadIntegerNode, self).__init__(ctx)
        self._value_type = PrimitiveTypes.Int

    def _run_type_check(self):
        pass  # No type check needed

    def _run_scope_check(self):
        pass  # No scope check needed

    def generate_code(self):
        self.ctx.text_segment += '\tli $v0, 5\n'
        self.ctx.text_segment += '\tsyscall\n'


class ReadLineNode(AbstractNode, ValuedNodeMixin):
    MAX_LINE_LENGTH = 500

    def __init__(self, ctx: NodeContext):
        super(ReadLineNode, self).__init__(ctx)
        self._value_type = PrimitiveTypes.string

    def _run_type_check(self):
        pass  # No type check needed

    def _run_scope_check(self):
        pass  # No scope check needed

    def generate_code(self):
        # allocate line buffer
        self.ctx.text_segment += f'\tli $a0, {self.MAX_LINE_LENGTH}\n'
        self.ctx.text_segment += f'\tli $v0, 9\n'
        self.ctx.text_segment += f'\tsyscall\n'
        # read into line buffer
        self.ctx.text_segment += f'\tmove $a0, $v0\n'
        self.ctx.text_segment += f'\tli $a1, {self.MAX_LINE_LENGTH}\n'
        self.ctx.text_segment += f'\tli $v0, 8\n'
        self.ctx.text_segment += f'\tsyscall\n'
        self.ctx.text_segment += f'\tmove $v0, $a0\n'
