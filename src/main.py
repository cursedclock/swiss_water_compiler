from webbrowser import get
from preprocessor import pre_process
from parser import get_parser

with open('test.txt', "r") as file:
    parser = get_parser()
    text = file.read()
    preprocessed_text = pre_process(text)
    result = parser.parse(preprocessed_text)
    print(result)
