import re
from collections import OrderedDict

_id_pattern = r'(?<![a-zA-Z0-9_]){}(?![a-zA-z0-9_])'

def pre_process(text: str) -> str:
    definitions = OrderedDict()
    lines = text.splitlines()
    processed_text = ''
    for line in lines:
        if re.match(r'\s*define [a-zA-Z][a-zA-Z0-9_]* .*', line):
            line = line.lstrip().split(' ', 2)
            definitions[line[1]] = line[2]
        else:
            processed_text += line+'\n'

    for definition in definitions:
        processed_text = re.sub(_id_pattern.format(definition),
                                definitions[definition],
                                processed_text)

    return processed_text
