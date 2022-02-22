define FOR_I_5 for (i = 0; i < 5; i += 1)
define FOR_J_5 for (j = 0; j < 5; j += 1)
define PRINT_I_J Print(i, j);

int main() {
	int i;
	int j;
	FOR_I_5 {
		FOR_J_5 {
			PRINT_I_J
		}
	}
}
