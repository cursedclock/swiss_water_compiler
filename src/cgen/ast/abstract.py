import enum


class NodeType(enum.Enum):
    ROOT = 1


class NodeContext:
    def __init__(self, symbol_table, text_segment, data_segment):
        self.symbol_table = symbol_table
        self.text_segment = text_segment
        self.data_segment = data_segment


class AbstractNode:
    def __init__(self, node_type: NodeType, ctx: NodeContext, children: [__class__] = None):
        if children is None:
            children = []
        else:
            self.children = children
        self.type = node_type
        self.ctx = ctx

    def run_type_check(self, raise_exception=False) -> bool:
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

    def run_scope_check(self, raise_exception=False) -> bool:
        try:
            self._run_type_check()
        except Exception as e:
            if raise_exception:
                raise e
            else:
                return False
        return True

    def _run_scope_check(self):
        raise NotImplementedError

    @property
    def symbol_table(self):
        return self.ctx.symbol_table


class ValuedNodeMixin:
    @property
    def value(self):
        raise NotImplementedError

    @property
    def value_type(self):
        raise NotImplementedError

