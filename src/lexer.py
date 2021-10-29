from ply import lex

# tuple of tokens
tokens = (
    'EQ',
    'LEQ',
    'GEQ',
    'NEQ',
    'PEQ',
    'MEQ',
    'TEQ',
    'DEQ',
    'AND',
    'OR',
    'BOOL',
    'BREAK',
    'BTOI',
    'CLASS',
    'CONTINUE',
    'DEFINE',
    'DOUBLE',
    'DTOI',
    'ELSE',
    'FOR',
    'IF',
    'IMPORT',
    'INT',
    'ITOB',
    'ITOD',
    'NEW',
    'NEWARRAY',
    'NULL',
    'PRINT',
    'PRIVATE',
    'PUBLIC',
    'READINTEGER',
    'READLINE',
    'RETURN',
    'STRING',
    'THIS',
    'VOID',
    'WHILE',
    'OP',
    'RESERVED',
    'BOOLEANLITERAL',
    'STRINGLITERAL',
    'DOUBLELITERAL',
    'INTLITERAL',
    'ID'
)

# used in parser
literals = [
    '=',
    '+',
    '-',
    '*',
    '/',
    '%',
    '<',
    '>',
    '!',
    ';',
    '.',
    ',',
    '(',
    ')',
    '[',
    ']',
    '{',
    '}',
]

# used for testing
double_op_tokens = [
    'EQ',
    'LEQ',
    'GEQ',
    'NEQ',
    'PEQ',
    'MEQ',
    'TEQ',
    'DEQ',
    'AND',
    'OR',
]

# used to differentiate keyword from ID
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

# used to differentiate keyword from ID
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
    r'(<=)|(>=)|(==?)|(\*=)|(\+=)|(-=)|(\/=)|(!=)|(&&)|(\|\|)|([+\-*\/%<>!;.,()\[\]{}])'
    if t.value == '==':
        t.type = 'EQ'
    elif t.value == '>=':
        t.type = 'GEQ'
    elif t.value == '<=':
        t.type = 'LEQ'
    elif t.value == '+=':
        t.type = 'PEQ'
    elif t.value == '-=':
        t.type = 'MEQ'
    elif t.value == '*=':
        t.type = 'TEQ'
    elif t.value == '/=':
        t.type = 'DEQ'
    elif t.value == '!=':
        t.type = 'NEQ'
    elif t.value == '||':
        t.type = 'OR'
    elif t.value == '&&':
        t.type = 'AND'
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = t.value.upper()
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

lexer = lex.lex()
