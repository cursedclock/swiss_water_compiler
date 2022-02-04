import sys, getopt

from parser import get_parser
from preprocessor import pre_process
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

    with open("tests/" + inputfile, "r") as input_file:
        parser = get_parser()
        text = input_file.read()
        preprocessed_text = pre_process(text)
        result = parser.parse(preprocessed_text)
        result.generate_code()


    with open("out/" + outputfile, "w+") as output_file:
        output_file.write(result.get_code())


if __name__ == "__main__":
    main(sys.argv[1:])
