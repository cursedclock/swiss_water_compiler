import os, sys
current_dir = os.getcwd()
src_dir = os.path.dirname(os.path.dirname(current_dir)) + '/src'
sys.path.append(src_dir)
from lexer import new_lexer

import getopt
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('main.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    lexer = new_lexer()
    outp = ''

    with open("tests/" + inputfile, "r") as input_file:
        lexer.input(input_file.read())
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type in ['RESERVED','OP']:
            outp += tok.value+'\n'
        else:
            outp += f'T_{tok.type} {tok.value}\n'
        
    

    with open("out/" + outputfile, "w") as output_file:
        # write result to output file. 
        # for the sake of testing : 
        output_file.write(outp)


if __name__ == "__main__":
    main(sys.argv[1:])
