from enum import Enum


class EntryType(Enum):
    Variable = 0
    Class = 1
    Func = 2


class SymbolTable:
    def __init__(self):
        self.scope_stack: [dict[str: object]] = [{}]
        self.context_stack: [dict[str: object]] = [{'__func__': ''}]

    def insert(self, key: str, item) -> None:
        if self.id_defined_in_scope(key):
            raise RuntimeError  # id already defined
        else:
            current_scope = self.scope_stack[-1]
            current_scope[key] = item

    def new_scope(self, ctx=None) -> None:
        ctx = ctx.copy() if ctx is not None else {'__func__': ''}
        self.context_stack.append(ctx)
        self.scope_stack.append({})

    def get(self, key: str) -> object:
        lookups = (self.scope_stack[i].get(key) for i in range(len(self.scope_stack)-1, -1, -1))
        for lookup in lookups:
            if lookup is not None:
                return lookup
        raise RuntimeError  # id not defined

    def get_type(self, key):
        entry = self.get(key)
        entry_type = entry.get(ENTRY_TYPE)
        if entry_type and entry_type is EntryType.Class:
            return entry
        else:
            raise RuntimeError  # identifier does not refer to type

    def get_from_ctx(self, key: str) -> object:
        lookups = (self.context_stack[i].get(key) for i in range(len(self.context_stack)-1, -1, -1))
        for lookup in lookups:
            if lookup is not None:
                return lookup
        return None

    def id_defined_in_scope(self, key: str) -> bool:
        return self.scope_stack[-1].get(key) is not None


# scope is in the form of Id: entry, which entry is a dict contains some info
# keys of this info
TYPE = 'type'
SIZE = 'size'
ENTRY_TYPE = 'entry_type'