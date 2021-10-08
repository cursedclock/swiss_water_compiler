import re
from collections import OrderedDict

_id_pattern = r'(^|\s|[^a-zA-Z0-9])({})(\s|$|[^a-zA-z0-9])'

def pre_process(text: str) -> str:
    definitions = OrderedDict()
    lines = text.splitlines()
    processed_text = ''
    for line in lines:
        if re.match(r'define \S+ .*', line):
            line = line.split(' ', 2)
            definitions[line[1]] = line[2]
        else:
            processed_text += line+'\n'

    for definition in definitions:
        for i in range(2):
            processed_text = re.sub(_id_pattern.format(definition),
                                    rf'\1{definitions[definition]}\3',
                                    processed_text)

    return processed_text
