void func__line__func() {
    int line;
    string func;
    int input;
    string out;

    func = __func__;
    line = __line__;
    Print("Function name: ", func);
    Print("Line number: ", line);
    if (line % 2 == 0) {
        out = "Line number plus input is even!";
    } else {
        out = "Line number plus input is odd!";
    }
    Print(out);
}
