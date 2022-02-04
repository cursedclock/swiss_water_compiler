from operator import truediv
from .abstract import AbstractNode
from .literal import PrimitiveTypes
from .utils import NodeContext

class ArrayType:
    def __init__(self, data_type):
        self.data_type = data_type


class TypeNode(AbstractNode):

    PRIMITIVES = ['int', 'string,', 'bool', 'double']

    def __init__(self, ctx: NodeContext, raw_type):
        super().__init__(ctx)
        self._type = self.get_type(raw_type)

    @property
    def type(self):
        return self._type

    def get_size(self):
        return 8 if self.type is PrimitiveTypes.Double else 4

    def _run_type_check(self):
        if not isinstance(self.type, PrimitiveTypes):
            self.symbol_table.get_type(self.type)

    def get_type(self, raw_type):
        try:
            return PrimitiveTypes[raw_type]
        except KeyError:
            return raw_type


class ArrayTypeNode(TypeNode):
    def _run_type_check(self):
        if not isinstance(self.type.data_type, PrimitiveTypes):
            self.symbol_table.get_type(self.type.data_type)

    def get_type(self, raw_type):
        data_type = super(ArrayTypeNode, self).get_type(raw_type)
        return ArrayType(data_type)
