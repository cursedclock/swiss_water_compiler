import ply.yacc as yacc
from lexer import tokens

def p_start(p):
    '''s : mac
         | empty'''
    if p[1] != None:
        p[0] = 'done'

def p_mac(p):
    '''mac : mac macro
           | macro'''
    p[0] = p[1]

def p_macro(p):
    '''macro : IMPORT STRINGLITERAL'''
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