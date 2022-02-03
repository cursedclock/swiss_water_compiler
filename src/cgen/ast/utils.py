from src.cgen.symbol_table import SymbolTable


class NodeContext:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.text_segment = '.text\n'
        self.data_segment = '.data\n'
        self.label_generator = LabelGenerator()


class LabelGenerator:
    def __init__(self):
        self.counter = 0

    def get_label(self):
        label = f'L{self.counter}'
        self.counter += 1
        return label


class ValuedNodeMixin:
    @property
    def value_type(self):
        return self._value_type

    def generate_code(self):
        """
        adds logic of getting the value of the node and storing it in $v0 to text and code segments
        """
        raise NotImplementedError