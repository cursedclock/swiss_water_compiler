

class SymbolTable:
    def __init__(self):
        self.scope_stack: [dict[str: object]] = [{}]
        self.context_stack: [dict[str: object]] = [{'__func__': ''}]

    def insert(self, key: str, item) -> None:
        top = self.scope_stack[-1]
        if top.get(key):
            raise RuntimeError  # id already defined
        else:
            top[key] = item

    def new_scope(self, ctx=None) -> None:
        if ctx is None:
            ctx = {'__func__': ''}
        else:
            self.context_stack.append(ctx.copy())
        self.scope_stack.append({})

    def get(self, key: str) -> object:
        lookups = (self.scope_stack[i].get(key) for i in range(len(self.scope_stack)-1, -1, -1))
        for lookup in lookups:
            if lookup is not None:
                return lookup
        raise RuntimeError  # id not defined

    def get_from_ctx(self, key: str) -> object:
        lookups = (self.context_stack[i].get(key) for i in range(len(self.context_stack)-1, -1, -1))
        for lookup in lookups:
            if lookup is not None:
                return lookup
        return None
