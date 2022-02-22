define funcName __func__
import "file-to-import.d"
define lineNumber __line__

int main() {
    int line;
    line = __line__;
    dummyVar = funcName;
    anotherFunction();
    Print("Function Name: ", dummyVar);
    Print(__func__ == funcName);
    Print(dummyVar != __func__)
    Print(lineNumber == line);
    Print(__line__ == lineNumber);
}

void anotherFunction() {
    Print("Function Name: ", funcName);
    Print(funcName == __func__, "\n");
}