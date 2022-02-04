from .abstract import AbstractNode


class BlockNode(AbstractNode):
    def _run_scope_check(self):
        pass  # no scope check needed

    def _run_type_check(self):
        pass  # no type echeck needed

    def generate_code(self):
        for child in self.children:
            child.generate_code()
