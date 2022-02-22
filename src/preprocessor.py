import re
from collections import OrderedDict

_id_pattern = r'(?<![a-zA-Z0-9_]){}(?![a-zA-Z0-9_])'

def pre_process(text: str) -> str:
    definitions = OrderedDict()
    lines = text.splitlines()
    processed_text = ''
    obey_grammar_order = True
    for line in lines:
        if re.match(r'\s*define.*', line):
            match = re.match(r'(\s*define\s*)([a-zA-Z][a-zA-Z0-9_]*)( )([^\s].*)', line)
            if match and obey_grammar_order:
                definitions[match.group(2)] = match.group(4)
            else:
                raise DefineError
        else:
            if not re.match(r'\s*import.*', line):
                obey_grammar_order = False
            processed_text += line+'\n'

    for definition in definitions:
        processed_text = re.sub(_id_pattern.format(definition),
                                definitions[definition],
                                processed_text)
    return processed_text

class DefineError(Exception):
    pass
