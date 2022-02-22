import os, sys, getopt

current_dir = os.getcwd()
src_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(src_dir)

from src import pre_process, get_parser, ParseError

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
    with open("out/" + outputfile, "w+") as output_file:
        try:
            with open("tests/" + inputfile, "r") as input_file:
                parser = get_parser()
                text = input_file.read()
                preprocessed_text = pre_process(text)
                result = parser.parse(preprocessed_text)
                result.generate_code()
                output_file.write(result.get_code())
        except ParseError as e:
                output_file.write('.data\nmsg:\t.asciiz\t"Syntax Error"\n'+
                                  '.text\nmain:\n\tla $a0, msg\n'+
                                  '\tli $v0, 4\n\tsyscall'+'\n\tli $v0, 10\n\tsyscall\n')
        except Exception as e:
                output_file.write('.data\nmsg:\t.asciiz\t"Semantic Error"\n'+
                                  '.text\nmain:\n\tla $a0, msg\n'+
                                  '\tli $v0, 4\n\tsyscall'+'\n\tli $v0, 10\n\tsyscall\n')



if __name__ == "__main__":
    main(sys.argv[1:])
