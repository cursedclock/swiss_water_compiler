from src.cgen.symbol_table import SymbolTable


class NodeContext:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.text_segment = r'.text	'+'\n'
        self.data_segment = r'.data	'+'\n'


class ValuedNodeMixin:
    @property
    def value_type(self):
        return self._value_type


    @property
    def value(self):
        return self._value