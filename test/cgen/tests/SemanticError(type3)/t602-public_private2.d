class A {
    public int a;
    private int c;
}

class B {
    public int d;
}

int main() {
    A a;
    B b;
    a = new A;
    a.a = 10;

    b = new B;
    b.d = 1;

    a.c = 3; // Error

    Print(a.a, " ", a.c, " ", b.d);

    return 0;
}