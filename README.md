# Swiss Water Compiler
A Decaf compiler targeting mips assembly written in pure python.

## Use
To use the compiler simply import `compile_decaf` and pass in the source code string as an argument.
The resulting assembly will be returned as a string.
```python3
from src import compile_decaf
with open('SRC_CODE_PATH') as f:
    code = f.read()
    output = compile_decaf(code)
    with open('OUTP_PATH', 'w+') as o:
        o.write(output)
```

## Tests
There are two test scrips kindly provided by the TA team for [Dr Bahrami's fall 2021 compiler design course](http://ce.sharif.edu/~mrbahrami/courses/CompilerFall21.html)
To run each set of tests change directories to the location of the script and run it.\
***Note: You will need the required packages in requirements.txt to run the lexer tests and spim to run the code-gen tests***

### Lexer Tests:
```bash
cd ./test/lexer
./run.sh
```

### Code Gen Tests:
```bash
cd ./test/cgen
./run.sh
```

## Development
**Currently Supports:**
- I/O statements
- variable declaration and assignment
- simple arithmetic operations

**Future Features:**
- Function declaration
- Class declaration
- Arrays