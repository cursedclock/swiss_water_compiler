import ply.yacc as yacc
from lexer import tokens

from cgen.ast import IntLiteralNode, NullLiteralNode, StringLiteralNode, DoubleLiteralNode, BoolLiteralNode,\
                     PrintStatementNode, ArrayTypeNode, TypeNode, VariableDeclarationNode, BlockNode, \
                     ReadLineNode, ReadIntegerNode, VarRefNode
from cgen.ast.utils import NodeContext
from cgen.ast.arithmetic import BinArithmeticNode
from cgen.ast.assignment import AssignmentNode

ctx = NodeContext()

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
    p[0] = BlockNode(ctx, p[2])


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
    '''macroStmt : IMPORT STRINGLITERAL'''
    p[0] = p[1]


# Decl+
def p_Decl(p):
    '''Decl : Decl declStmt'''
    p[1].append(p[2])
    p[0] = p[1]

def p_Decl_Base(p):
    '''Decl : declStmt'''
    p[0] = [p[1]]

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
    node = VariableDeclarationNode(ctx, [p[1], p[2]])
    node.run_scope_check()
    p[0] = node


# Type
def p_Type_Single(p):
    """Type : INT
            | DOUBLE
            | BOOL
            | STRING
            | ID"""
    p[0] = TypeNode(ctx, p[1])


def p_Type_Array(p):
    """Type : INT OBRACKET CBRACKET
            | DOUBLE OBRACKET CBRACKET
            | BOOL OBRACKET CBRACKET
            | STRING OBRACKET CBRACKET
            | IdBrack CBRACKET"""
    p[0] = ArrayTypeNode(ctx, p[1])


def p_IdBrack(p):
    '''IdBrack : ID OBRACKET'''
    p[0] = p[1]


# FunctionDecl
def p_FunctionDecl(p):
    '''FunctionDecl : FunctionDeclInit StmtBlock'''
    ctx.symbol_table.pop_scope()
    p[0] = p[2]


# FunctionDecl
def p_FunctionDeclInit(p):
    '''FunctionDeclInit : Type ID OPAREN Formals CPAREN
                        | VOID ID OPAREN Formals CPAREN'''
    ctx.symbol_table.new_scope({'__func__': p[2]})
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
    '''StmtBlock : OBRACE block CBRACE'''
    p[0] = p[2]


def p_block(p):
    """block : varDclBlock stmtStmtBlock
             | stmtStmtBlock"""
    if len(p) == 3:
        p[0] = BlockNode(ctx, p[1] + p[2])
    else:
        p[0] = BlockNode(ctx, p[1])


def p_varDclBlock(p):
    '''varDclBlock : varDclBlock VariableDecl'''
    p[1].append(p[2])
    p[0] = p[1]

def p_varDclBlock_Base(p):
    '''varDclBlock : VariableDecl'''
    p[0] = [p[1]]

def p_stmtStmtBlock(p):
    '''stmtStmtBlock : stStBlock'''
    p[0] = p[1]

def p_stmtStmtBlock_Base(p):
    '''stmtStmtBlock :  empty'''
    p[0] = []

def p_stStBlock(p):
    '''stStBlock : stStBlock Stmt'''
    p[1].append(p[2])
    p[0] = p[1]

def p_stStBlock_Base(p):
    '''stStBlock :  Stmt'''
    p[0] = [p[1]]


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
    p[0] = p[1]


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
    p[0] = PrintStatementNode(ctx, p[3])


def p_exprArg_Repeat(p):
    """exprArg : exprArg COMMA Expr"""
    p[1].append(p[3])
    p[0] = p[1]


def p_exprArg_Base(p):
    """exprArg : Expr"""
    p[0] = [p[1]]


# Expr?
def p_optionalExpr(p):
    '''optionalExpr : Expr
                    | empty'''
    p[0] = p[1]


# Expr
def p_Expr_other(p):
    '''Expr : LValue
            | THIS
            | Call
            | OPAREN Expr CPAREN
            | Expr binOp Expr
            | MINUS Expr %prec UMINUS
            | EXCL Expr
            | NEW ID
            | NEWARRAY OPAREN Expr COMMA Type CPAREN
            | ITOD OPAREN Expr CPAREN
            | DTOI OPAREN Expr CPAREN
            | ITOB OPAREN Expr CPAREN
            | BTOI OPAREN Expr CPAREN
            | __LINE__
            | __FUNC__'''
    if len(p) > 3:
        p[0] = BinArithmeticNode(ctx, [p[1], p[2], p[3]])
    else:
        p[0] = p[1]


def p_Expr_Read(p):
    '''Expr : READINTEGER OPAREN CPAREN
            | READLINE OPAREN CPAREN'''
    p[0] = ReadLineNode(ctx) if p[1] == 'ReadLine' else ReadIntegerNode(ctx)

def p_Expr_IntLiteral(p):
    """Expr : INTLITERAL"""
    p[0] = IntLiteralNode(ctx, 'INTLITERAL', int(p[1]))


def p_Expr_DoubleLiteral(p):
    """Expr : DOUBLELITERAL"""
    p[0] = DoubleLiteralNode(ctx, 'DOUBLELITERAL', p[1])


def p_Expr_BOOLEANLITERAL(p):
    """Expr : BOOLEANLITERAL"""
    p[0] = BoolLiteralNode(ctx, 'BOOLEANLITERAL', p[1])


def p_Expr_STRINGLITERAL(p):
    """Expr : STRINGLITERAL"""
    p[0] = StringLiteralNode(ctx, 'STRINGLITERAL', p[1])


def p_Expr_Null(p):
    """Expr : NULL"""
    p[0] = NullLiteralNode(ctx, 'NULL', p[1])


def p_Expr_Assignment(p):
    '''Expr : LValue assignment Expr'''
    p[0] = AssignmentNode(ctx, [p[1], p[3]])


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
              | IdBrack Expr CBRACKET
              | Expr OBRACKET Expr CBRACKET'''
    p[0] = VarRefNode(ctx, p[1])


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


# related to ply
def p_empty(p):
    '''empty : '''
    pass


# error handling
def p_error(p):
    # also, we can have an error list, to check whether syntax analysis was successful or not
    if p:
         print(f'Syntax error at token {p.type} at line {p.lineno}')
         # Just discard the token and tell the parser it's okay.
         parser.errok()
    else:
         print("Syntax error at EOF")



parser = yacc.yacc()

def get_parser():
    return parser

def new_parser():
    return yacc.yacc()
