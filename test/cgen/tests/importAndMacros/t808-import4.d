import "file-to-import2.d"

int main() {
    int a;
    int b;
    int c;
    int result1;
    int result2;

    a = ReadInteger();
    b = ReadInteger();
    c = ReadInteger();

    Calc cal;
    cal = new Calc;

    result1 = cal.add(cal.sub(0, b), cal.div(cal.delta(a,b,c), cal.mult(2, a)));
    result2 = cal.sub(cal.sub(0, b), cal.div(cal.delta(a,b,c), cal.mult(2, a)));
    Print(cal.res - result1);
}

