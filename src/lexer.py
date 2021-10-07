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

t_OP = r'([+\-*%<>!;.,()\[\]{}])|(<=)|(>=)|(==?)|(\+=)|(-=)|(\/=)|(!=)|(&&)|(\|\|)'
t_RESERVED = r'(__func__)|(__line__)|(bool)|(break)|(btoi)|(class)|(continue)|(define)|(double)|(dtoi)|(else)|(for)|(if)|(import)|(int)|(itob)|(itod)|(new)|(NewArray)|(null)|(Print)|(private)|(public)|(ReadInteger)|(ReadLine)|(return)|(string)|(this)|(void)|(while)'
t_BOOLEANLITERAL = r'(true)|(false)'
t_STRINGLITERAL = r'\"[^\n"]*\"'
t_DOUBLELITERAL = r'[0-9]+\.[0-9]*((e|E)\+[0-9]+)?'
t_INTLITERAL = r'(0(x|X)[0-9a-fA-F]+)|([0-9]+)'
t_ID = r'[a-zA-Z][a-zA-Z0-9_]*'
t_ignore_COMMENT = r'\/\/.*'
t_ignore_MULTICOMEMNT = r'\/\*((?!\*\/)(.|\n))*\*\/'
t_ignore  = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def new_lexer():
    return lex.lex()
