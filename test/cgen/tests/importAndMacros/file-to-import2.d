class Calc {
    public int res;

    public int add(int a, int b) {
        res = a + b;
        return res;
    }

    public int sub(int a, int b) {
        res = a - b;
        return res;
    }
    
    public int mult(int a, int b) {
        res = a * b;
        return res;
    }

    public int div(int a, int b) {
        res = a / b;
        return res;
    }

    public int rem(int a, int b) {
        res = a % b;
        return res;
    }

    public int delta(int a, int b, int c) {
        return sub(add(0, mult(b, b)), mult(mult(4, a), c));
    }
}