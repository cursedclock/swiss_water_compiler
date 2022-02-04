from src.cgen.ast.abstract import AbstractNode
from src.cgen.ast.literal import PrimitiveTypes
from src.cgen.ast.utils import NodeContext, ValuedNodeMixin


class BinArithmeticNode(AbstractNode, ValuedNodeMixin):

    # child 0 -> leftOp, 1 -> operator, 2 -> rightOp
    def __init__(self, ctx: NodeContext, children):
        super().__init__(ctx, children)
        self._value_type = self.children[0].value_type
        # self.run_type_check(True)

    def _run_type_check(self):
        if self.children[0].value_type != PrimitiveTypes.Int or self.children[2].value_type != PrimitiveTypes.Int:
            print(self.children[0].value_type)
            print(PrimitiveTypes.Int)
            raise Exception

    def generate_code(self):
        self.children[0].generate_code()
        self.ctx.text_segment += f'\tmove $t0, $v0\n'

        self.children[2].generate_code()
        self.ctx.text_segment += f'\tmove $t1, $v0\n'

        if self.children[1] == '+':
            self.ctx.text_segment += f'\tadd $v0, $t0, $t1\n'
        if self.children[1] == '-':
            self.ctx.text_segment += f'\tsub $v0, $t0, $t1\n'
        if self.children[1] == '*':
            self.ctx.text_segment += f'\tmul $v0, $t0, $t1\n'
        if self.children[1] == '/':
            self.ctx.text_segment += f'\tdiv $v0, $t0, $t1\n'

    def get_value(self):
        if self.children[1] == '+':
            return self.children[0].get_value() + self.children[2].get_value()
        if self.children[1] == '-':
            return self.children[0].get_value() - self.children[2].get_value()
        if self.children[1] == '*':
            return self.children[0].get_value() * self.children[2].get_value()
        if self.children[1] == '/':
            return self.children[0].get_value() / self.children[2].get_value()