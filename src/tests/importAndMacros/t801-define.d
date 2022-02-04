define PI 3
define FOR_5_WITH_I for (i = 0; i < 5; i += 1)

int main() {
	int i;
	Print("Printing PI for 5 times...");
	FOR_5_WITH_I {
		Print(PI + i);
	}
}
