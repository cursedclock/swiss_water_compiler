from .abstract import AbstractNode
from .utils import ValuedNodeMixin, NodeContext
from .literal import PrimitiveTypes
from src.cgen.symbol_table import TYPE


class VarRefNode(AbstractNode, ValuedNodeMixin):
    def __init__(self, ctx: NodeContext, var_name: str):
        super(VarRefNode, self).__init__(ctx)
        self.var_name = var_name
        st_entry = self.symbol_table.get_var(var_name)
        self._value_type = st_entry[TYPE]
        self.depth = self.symbol_table.get_depth(var_name)

    def _run_type_check(self):
        pass  # not type check needed

    def _run_scope_check(self):
        pass  # no scope check needed

    def generate_code(self):
        if self.value_type is PrimitiveTypes.Double:
            self.ctx.text_segment += f'\tl.d $f0, {self.depth}($sp)\n'
        else:
            self.ctx.text_segment += f'\tlw $v0, {self.depth}($sp)\n'
