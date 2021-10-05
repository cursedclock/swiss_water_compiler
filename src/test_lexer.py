from lexer import new_lexer

data = '''
define PI 3.14
define FOR100 for (i=0; i< 100; i++)
int main(){
    int i;
    FOR100 {
        Print(i, PI);
    }
    if i===2{
    }
}'''

my_lexer = new_lexer()
my_lexer.input(data)
tok = True
while tok:
    tok = my_lexer.token()
    print(tok)