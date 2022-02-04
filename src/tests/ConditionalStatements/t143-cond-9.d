
int main() {
    bool b;
    b = false;
    b = (true && (false || b)) || true;
    if (b == true) Print("true");
    else Print("false");
    if (b == false) Print("true");
    else Print("false");
}
