from ply import lex

# tuple of tokens
tokens = (
    'ASSIGN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PERCENT',
    'LESS',
    'GREATER',
    'SEMICOLON',
    'EXCL',
    'DOT',
    'COMMA',
    'OPARAN',
    'CPARAN',
    'OBRACKET',
    'CBRACKET',
    'OBRACE',
    'CBRACE',
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
    '__FUNC__',
    '__LINE__',
    'OP',
    'BOOLEANLITERAL',
    'STRINGLITERAL',
    'DOUBLELITERAL',
    'INTLITERAL',
    'ID'
)

op_tokens = { 
    '=': 'ASSIGN',
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'TIMES',
    '/': 'DIVIDE',
    '%': 'PERCENT',
    '<': 'LESS',
    '>': 'GREATER',
    '!': 'EXCL',
    ';': 'SEMICOLON',
    '.': 'DOT',
    ',': 'COMMA',
    '(': 'OPAREN',
    ')': 'CPAREN',
    '[': 'OBRACKET',
    ']': 'CBRACKET',
    '{': 'OBRACE',
    '}': 'CBRACE',
    '==': 'EQ',
    '<=': 'LEQ',
    '>=': 'GEQ',
    '!=': 'NEQ',
    '+=': 'PEQ',
    '-=': 'MEQ',
    '*=': 'TEQ',
    '/=': 'DEQ',
    '&&': 'AND',
    '||': 'OR',
}

# used to differentiate keyword from ID
reserved = [
    '__line__',
    '__func__',
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
    if t.value in op_tokens:
        t.type = op_tokens[t.value]
    return t

def t_ID(t):
    r'([a-zA-Z][a-zA-Z0-9_]*)|(__func__)|(__line__)'
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
