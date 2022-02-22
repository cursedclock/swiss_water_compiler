from .lexer import new_lexer
from .preprocessor import pre_process
from .parser import get_parser, ParseError


def compile_decaf(code: str) -> str:
    pre_code = pre_process(code)
    parser = get_parser()
    return parser.parse(pre_code).generate_code()
