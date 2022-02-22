define PRINT_I_FUNCTION void printer(int input) { Print(input); }
define GET_INT_INPUT ReadInteger()

PRINT_I_FUNCTION

int main() {
	int i;
	i = GET_INT_INPUT;
	printer(i);
}
