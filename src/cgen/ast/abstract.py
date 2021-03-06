from __future__ import annotations
import enum
from .utils import NodeContext


class NodeType(enum.Enum):
    ROOT = 1


class AbstractNode:
    def __init__(self, ctx: NodeContext, children: [AbstractNode] = None):
        self.children = children if children is not None else []
        self.ctx = ctx

    def run_type_check(self, raise_exception=True) -> bool:
        try:
            self._run_type_check()
        except Exception as e:
            if raise_exception:
                raise e
            else:
                return False
        return True

    def _run_type_check(self):
        raise NotImplementedError

    def run_scope_check(self, raise_exception=True) -> bool:
        try:
            self._run_scope_check()
        except Exception as e:
            if raise_exception:
                raise e
            else:
                return False
        return True

    def _run_scope_check(self):
        raise NotImplementedError

    def validate_semantics(self, raise_exception=True) -> bool:
        try:
            self._run_type_check()
            self._run_scope_check()
        except Exception as e:
            if raise_exception:
                raise e
            else:
                return False
        return True


    def generate_code(self):
        raise NotImplementedError

    @property
    def symbol_table(self):
        return self.ctx.symbol_table

    def get_code(self):
        return self.ctx.data_segment+'\n'+self.ctx.text_segment+'\n'+'\tli $v0, 10\n\tsyscall\n'+'''
print_nl:
	la $a0, NEWLINE
	li $v0, 4
	syscall
	jr	$ra
'''
