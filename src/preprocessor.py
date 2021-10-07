import re
from collections import OrderedDict


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
        processed_text = processed_text.replace(definition, definitions[definition])

    return processed_text
