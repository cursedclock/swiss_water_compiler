from cgen.ast.abstract import AbstractNode
from cgen.ast.utils import NodeContext
from cgen.symbol_table import TYPE, SIZE,ENTRY_TYPE, EntryType


class VariableDeclarationNode(AbstractNode):

    # children[0] is Type and [1] is ID
    def __init__(self, ctx: NodeContext, children: [AbstractNode] = None):
        super().__init__(ctx, children)
        self.var_size = self.children[0].get_size()

    def _run_scope_check(self):
        if self.symbol_table.id_defined_in_scope(self.children[1]):
            raise Exception
        else:
            self.symbol_table.insert(self.children[1], {TYPE: self.children[0].type,
                                                        SIZE: self.var_size,
                                                        ENTRY_TYPE: EntryType.Variable})

    def generate_code(self):
        self.ctx.text_segment += f'\taddi $sp, $sp, -{self.var_size}\n'
