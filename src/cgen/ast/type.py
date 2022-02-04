from operator import truediv
from src.cgen.ast.abstract import AbstractNode
from src.cgen.ast.utils import NodeContext


class TypeNode(AbstractNode):

    PRIMITIVES = ['int', 'string,', 'bool', 'double']

    def __init__(self, ctx: NodeContext, raw_type):
        super().__init__(ctx, None)
        self._type = raw_type
        self.is_primitive = raw_type in self.PRIMITIVES

    @property
    def type(self):
        return self._type

    def get_size(self):
        return 8 if self.type == 'double' else 4

    def _run_type_check(self):
        if self.is_primitive:
            return True
