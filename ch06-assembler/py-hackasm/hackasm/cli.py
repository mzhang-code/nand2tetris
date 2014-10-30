# -*- coding: utf-8 -*- 
# Author    :   Mengyu Zhang (mengyuzhang@uchicago.edu) 
# Date      :   Oct 30 2014 

import os 
import sys 
import argparse 
from hackasm.parser import Parser

def arg_parse(): 
    arg_parser = argparse.ArgumentParser(description='The Hack Assembler.')
    arg_parser.add_argument("asm_file",
            help='The path of input asm source file.') 

    arg_parser.add_argument("-o", "--output", 
            help='Specify the output file name, default is *stdout*') 

    return arg_parser.parse_args()

def main(): 
    args = arg_parse() 
    parser = Parser() 
    if args.output: 
        sys.stdout = open(args.output, 'w') 
    with open(args.asm_file, 'r') as f: 
        insts = parser.parse(f.readlines()) 
        print '\n'.join(insts) 
    
if __name__ == '__main__': 
    main() 

