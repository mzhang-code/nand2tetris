import os 
import pytest 

from hackasm.parser import Parser

TEST_DIR = os.path.dirname(__file__)

def test_preprocess(): 
    parser = Parser() 
    with open(os.path.join(TEST_DIR, 'asm', 'Max.asm'), 'r') as f:
        lines = f.readlines() 
        mod_lines = parser.preprocess(lines) 
        assert mod_lines == [
                    '@0', 
                    'D=M', 
                    '@1', 
                    'D=D-M', 
                    '@OUTPUT_FIRST', 
                    'D;JGT', 
                    '@1', 
                    'D=M', 
                    '@OUTPUT_D', 
                    '0;JMP', 
                    '(OUTPUT_FIRST)', 
                    '@0', 
                    'D=M', 
                    '(OUTPUT_D)', 
                    '@2', 
                    'M=D', 
                    '(INFINITE_LOOP)', 
                    '@INFINITE_LOOP', 
                    '0;JMP'] 

def test_parse(): 
    parser = Parser() 
    # Add.asm
    lines = ['@2', 'D=A', '@3', 'D=D+A', '@0', 'M=D'] 
    insts = parser.parse(lines) 

    assert insts == ['0000000000000010', 
                     '1110110000010000', 
                     '0000000000000011', 
                     '1110000010010000', 
                     '0000000000000000', 
                     '1110001100001000']

    # Max.asm 
    with open(os.path.join(TEST_DIR, 'asm', 'Max.asm'), 'r') as f:
        lines = f.readlines() 
        insts = parser.parse(lines) 
        assert insts == ['0000000000000000',  
                        '1111110000010000', 
                        '0000000000000001', 
                        '1111010011010000', 
                        '0000000000001010', 
                        '1110001100000001', 
                        '0000000000000001', 
                        '1111110000010000', 
                        '0000000000001100', 
                        '1110101010000111', 
                        '0000000000000000', 
                        '1111110000010000', 
                        '0000000000000010', 
                        '1110001100001000', 
                        '0000000000001110', 
                        '1110101010000111']

