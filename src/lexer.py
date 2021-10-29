from ply import lex

# tuple of tokens
tokens = (
    'OP',
    'RESERVED',
    'BOOLEANLITERAL',
    'STRINGLITERAL',
    'DOUBLELITERAL',
    'INTLITERAL',
    'ID'
)

reserved = [
    'bool',
    'break',
    'btoi',
    'class',
    'continue',
    'define',
    'double',
    'dtoi',
    'else',
    'for',
    'if',
    'import',
    'int',
    'itob',
    'itod',
    'new',
    'NewArray',
    'null',
    'Print',
    'private',
    'public',
    'ReadInteger',
    'ReadLine',
    'return',
    'string',
    'this',
    'void',
    'while'
]

boolean_literals = ['true', 'false']

t_RESERVED = r'(__func__)|(__line__)'
t_STRINGLITERAL = r'"([^"\\]|\\.)*"'
t_DOUBLELITERAL = r'[0-9]+\.[0-9]*((e|E)(\+|\-)?[0-9]+)?'
t_INTLITERAL = r'(0(x|X)[0-9a-fA-F]+)|([0-9]+)'
t_ignore = ' \t'

def t_COMMENT(t):
    r'\/\/.*'

def t_MULTICOMEMNT(t):
    r'\/\*((?!\*\/)(.|\n))*\*\/'

def t_OP(t):
    r'(<=)|(>=)|(==?)|(\*=)|(\+=)|(-=)|(\/=)|(!=)|(&&)|(>=)|(<=)|(\|\|)|([+\-*\/%<>!;.,()\[\]{}])'
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = 'RESERVED'
    elif t.value in boolean_literals:
        t.type = 'BOOLEANLITERAL'
    return t
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def new_lexer():
    return lex.lex()
