import ply.yacc as yacc
from lexer import tokens


# Program
def p_Program(p):
    '''Program : Macro Decl'''
    if p[2] != None:
        p[0] = 'done'


# Macro
def p_Macro(p):
    '''Macro : macro
             | empty'''
    p[0] = p[1]

def p_macro(p):
    '''macro : macro macroStmt
             | macroStmt'''
    p[0] = p[1]

def p_macroStmt(p):
    '''macroStmt : IMPORT STRINGLITERAL
                 | DEFINE ID defineStmt'''
    p[0] = p[1]

# how to implement * ?
def p_defineStmt(p):
    '''defineStmt : ID'''
    p[0] = p[1]


# Decl
def p_Decl(p):
    '''Decl : Decl declStmt
           | declStmt'''
    p[0] = p[1]

def p_declStmt(p):
    '''declStmt : VariableDecl'''
    p[0] = p[1]


# VariableDecl
def p_VariableDecl(p):
    '''VariableDecl : Variable SEMICOLON'''
    p[0] = p[1]


# Variable
def p_Variable(p):
    '''Variable : Type ID'''
    p[0] = p[1]


# Type
def p_Type(p):
    '''Type : INT
            | DOUBLE
            | BOOL
            | STRING
            | ID
            | Type OBRACKET CBRACKET'''
    p[0] = p[1]


# related to ply
def p_empty(p):
    'empty :'
    pass

# def p_error(p):
#     pass

parser = yacc.yacc()

with open("test.txt", "r") as file:
   result = parser.parse(file.read())
   print(result)