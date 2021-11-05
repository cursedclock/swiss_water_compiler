import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('right', 'ASSIGN', 'PEQ', 'MEQ', 'TEQ', 'DEQ'),  # assignments
    ('left', 'OR'),  # logical
    ('left', 'AND'),  # logical
    ('nonassoc', 'EQ', 'NEQ'),  # comparison
    ('nonassoc', 'GREATER', 'LESS', 'LEQ', 'GEQ'),  # comparison
    ('left', 'PLUS', 'MINUS'),  # add minus
    ('left', 'TIMES', 'DIVIDE', 'PERCENT'),  # division mult
    ('right', 'UMINUS', 'EXCL'),  # unary
    ('left', 'DOT', 'OBRACKET'),
)


# Program
def p_Program(p):
    '''Program : Macro Decl'''
    if p[2] != None:
        p[0] = 'done'


# Macro*
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


# Decl+
def p_Decl(p):
    '''Decl : Decl declStmt
            | declStmt'''
    p[0] = p[1]

def p_declStmt(p):
    '''declStmt : VariableDecl
                | FunctionDecl
                | ClassDecl'''
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


# FunctionDecl
def p_FunctionDecl(p):
    '''FunctionDecl : Type ID OPAREN Formals CPAREN StmtBlock
                    | VOID ID OPAREN Formals CPAREN StmtBlock'''
    p[0] = p[1]


# Formals
def p_Formals(p):
    '''Formals : varFormals
               | empty'''
    p[0] = p[1]

def p_varFormals(p):
    '''varFormals : varFormals COMMA Variable
                  | Variable'''
    p[0] = p[1]


# ClassDecl
def p_ClassDecl(p):
    '''ClassDecl : CLASS ID OBRACE Field CBRACE'''
    p[0] = p[1]


# Field
def p_Field(p):
    '''Field : field
             | empty'''
    p[0] = p[1]

def p_field(p):
    '''field : field fieldStmt
             | fieldStmt'''
    p[0] = p[1]

def p_fieldStmt(p):
    '''fieldStmt : AccessMode VariableDecl
                 | AccessMode FunctionDecl'''
    p[0] = p[1]


# AccessMode
def p_AccessMode(p):
    '''AccessMode : PRIVATE
                  | PUBLIC
                  | empty'''
    p[0] = p[1]


# StmtBlock
def p_StmtBlock(p):
    '''StmtBlock : OBRACE variableDeclStmtBlock stmtStmtBlock CBRACE'''
    p[0] = p[1]

def p_variableDeclStmtBlock(p):
    '''variableDeclStmtBlock : varDclBlock
                             | empty'''
    p[0] = p[1]

def p_varDclBlock(p):
    '''varDclBlock : varDclBlock VariableDecl
                   | VariableDecl'''
    p[0] = p[1]

def p_stmtStmtBlock(p):
    '''stmtStmtBlock : stStBlock
                     | empty'''
    p[0] = p[1]

def p_stStBlock(p):
    '''stStBlock : stStBlock Stmt
                 | Stmt'''
    p[0] = p[1]


# Stmt
def p_Stmt(p):
    '''Stmt : optionalExpr SEMICOLON
            | IfStmt
            | WhileStmt
            | ForStmt
            | BreakStmt
            | ContinueStmt
            | ReturnStmt
            | PrintStmt
            | StmtBlock'''
    p[0] =p[1]


# IfStmt
def p_IfStmt(p):
    '''IfStmt : IF OPAREN Expr CPAREN Stmt optionalElseStmt'''
    p[0] = p[1]

def p_optionalElseStmt(p):
    '''optionalElseStmt : ELSE Stmt
                        | empty'''
    p[0] = p[1]


# WhileStmt
def p_WhileStmt(p):
    '''WhileStmt : WHILE OPAREN Expr CPAREN Stmt'''
    p[0] = p[1]


# ForStmt
def p_ForStmt(p):
    '''ForStmt : FOR OPAREN optionalExpr SEMICOLON Expr SEMICOLON optionalExpr CPAREN Stmt'''
    p[0] = p[1]


# ReturnStmt
def p_ReturnStmt(p):
    '''ReturnStmt : RETURN optionalExpr SEMICOLON'''
    p[0] = p[1]


# BreakStmt
def p_BreakStmt(p):
    '''BreakStmt : BREAK SEMICOLON'''
    p[0] = p[1]


# ContinueStmt
def p_ContinueStmt(p):
    '''ContinueStmt : CONTINUE SEMICOLON'''
    p[0] = p[1]


# PrintStmt
def p_PrintStmt(p):
    '''PrintStmt : PRINT OPAREN exprArg CPAREN SEMICOLON'''
    p[0] = p[1]

def p_exprArg(p):
    '''exprArg : exprArg COMMA Expr
               | Expr'''
    p[0] = p[1]


# Expr?
def p_optionalExpr(p):
    '''optionalExpr : Expr
                    | empty'''
    p[0] = p[1]


# Expr
def p_Expr(p):
    '''Expr : LValue assignment Expr
            | Constant
            | LValue
            | THIS
            | Call
            | OPAREN Expr CPAREN
            | Expr binOp Expr
            | MINUS Expr %prec UMINUS
            | EXCL Expr
            | READINTEGER OPAREN CPAREN
            | READLINE OPAREN CPAREN
            | NEW ID
            | NEWARRAY OPAREN Expr COMMA Type CPAREN
            | ITOD OPAREN Expr CPAREN
            | DTOI OPAREN Expr CPAREN
            | ITOB OPAREN Expr CPAREN
            | BTOI OPAREN Expr CPAREN
            | __LINE__
            | __FUNC__'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : ASSIGN
                  | PEQ
                  | MEQ
                  | TEQ
                  | DEQ'''
    p[0] = p[1]

def p_binOp(p):
    '''binOp : PLUS
             | MINUS
             | TIMES
             | DIVIDE
             | PERCENT
             | LESS
             | GREATER
             | EQ
             | LEQ
             | GEQ
             | NEQ
             | AND
             | OR'''
    p[0] = p[1]


# LValue
def p_LValue(p):
    '''LValue : ID
              | Expr DOT ID
              | Expr OBRACKET Expr CBRACKET'''
    p[0] = p[1]


# Call
def p_Call(p):
    '''Call : ID OPAREN Actuals CPAREN
            | Expr DOT ID OPAREN Actuals CPAREN'''
    p[0] = p[1]


# Actuals
def p_Actuals(p):
    '''Actuals : exprActuals
               | empty'''
    p[0] = p[1]

def p_exprActuals(p):
    '''exprActuals : exprActuals COMMA Expr
                   | Expr'''
    p[0] = p[1]


# Constant
def p_Constant(p):
    '''Constant : INTLITERAL
                | DOUBLELITERAL
                | BOOLEANLITERAL
                | STRINGLITERAL
                | NULL'''
    p[0] = p[1]


# related to ply
def p_empty(p):
    '''empty : '''
    pass

# def p_error(p):
#     pass

parser = yacc.yacc()

with open("test.txt", "r") as file:
   result = parser.parse(file.read())
   print(result)