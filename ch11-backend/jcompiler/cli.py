
import re
import os 
import sys 

from jcompiler.token import tokenize
from jcompiler.parse import Parser

def remove_comments(s): 
    return re.sub(r'(\s*//.*)|(\s*/\*(.|\n)*?\*/\s*)', '', s) 

if __name__ == '__main__': 
    
    if len(sys.argv) < 2: 
        print 'a input file is needed'
        sys.exit(1)

    fname = sys.argv[1]
    if not os.path.isfile(fname): 
        print 'not a valid file path: %s' % fname 
        sys.exit(1) 

    with open(fname, 'r') as f: 
        source = remove_comments(f.read()) 
        parser = Parser(tokenize(source))
        tree = parser.parse_tree() 
        print tree 

