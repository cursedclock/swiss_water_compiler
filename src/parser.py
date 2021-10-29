import ply.yacc as yacc
from lexer import tokens

def p_Start(p):
    '''S : Macro'''
    if p[1] != None:
        p[0] = 'done'

def p_Macro(p):
    '''Macro : macro
            | empty'''
    p[0] = p[1]

def p_macro(p):
    '''macro : macro macroStmt
           | macroStmt'''
    p[0] = p[1]

def p_macroStmt(p):
    '''macroStmt : IMPORT STRINGLITERAL'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

# def p_error(p):
#     pass

parser = yacc.yacc()

with open("test.txt", "r") as file:
   result = parser.parse(file.read())
   print(result)