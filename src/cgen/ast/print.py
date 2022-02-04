from .abstract import AbstractNode
from .utils import ValuedNodeMixin, NodeContext
from .literal import PrimitiveTypes


class PrintStatementNode(AbstractNode):
    def __init__(self, ctx: NodeContext, children: [ValuedNodeMixin] = None):
        super(PrintStatementNode, self).__init__(ctx, children)
        self.validate_semantics()

    def _run_scope_check(self):
        pass  # no checks needed

    def _run_type_check(self):
        if any((v.value_type is not PrimitiveTypes for v in self.children)):
            raise RuntimeError  # Print value must be a primitive

    def generate_code(self):
        for valued_node in self.children:
            valued_node.generate_code()
            value_type = valued_node.value_type
            {
                PrimitiveTypes.Int:     self.print_int,
                PrimitiveTypes.Bool:    self.print_bool,
                PrimitiveTypes.String:  self.print_string,
                PrimitiveTypes.Null:    self.print_null,
                PrimitiveTypes.Double:  self.print_double
            }.get(value_type,           self.print_obj)()

    def print_int(self):
        self.ctx.text_segment += f'\tmove $a0, $v0\n'
        self.ctx.text_segment += f'\tli $v0, 1\n'
        self.ctx.text_segment += f'\tsyscall\n'

    def print_bool(self):
        label = self.ctx.label_generator.get_label()
        self.ctx.text_segment += f'\tla $a0, FALSE\n'
        self.ctx.text_segment += f'\tbeqz $v0, {label}\n'
        self.ctx.text_segment += f'\tla $a0, TRUE\n'
        self.ctx.text_segment += f'{label}:\tli $v0, 4\n'
        self.ctx.text_segment += f'\tsyscall\n'

    def print_string(self):
        self.ctx.text_segment += f'\tmove $a0, $v0\n'
        self.ctx.text_segment += f'\tli $v0, 4\n'
        self.ctx.text_segment += f'\tsyscall\n'

    def print_double(self):
        self.ctx.text_segment += f'\tmov.d $f12, $f0\n'
        self.ctx.text_segment += f'\tli $v0, 3\n'
        self.ctx.text_segment += f'\tsyscall\n'

    def print_null(self):
        self.ctx.text_segment += f'\tla $a0, NULL\n'
        self.ctx.text_segment += f'\tli $v0, 4\n'
        self.ctx.text_segment += f'\tsyscall\n'

    def print_obj(self):
        raise NotImplementedError # TODO implement print object
