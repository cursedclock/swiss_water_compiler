from src.cgen.ast.abstract import AbstractNode
from src.cgen.ast.utils import NodeContext
from src.cgen.symbol_table import TYPE, VALUE


class AssignmentNode(AbstractNode):

    def __init__(self, ctx: NodeContext, children: [AbstractNode] = None):
        super().__init__(ctx, children)
        self.id_entry = None
        self.run_scope_check(True)
        self.run_type_check(True)

    def _run_scope_check(self):
        entry = self.symbol_table.get(self.children[0].var_name)
        self.id_entry = entry

    def _run_type_check(self):
        if self.id_entry.get(TYPE) != self.children[1].value_type:
            raise Exception
        self.id_entry[VALUE] = self.children[1]._literal_value

    def generate_code(self):
        self.children[1].generate_code()
        offset = self.symbol_table.get_depth(self.children[0].var_name)
        self.ctx.text_segment += f'\tsw $v0, {offset}($sp)\n'
