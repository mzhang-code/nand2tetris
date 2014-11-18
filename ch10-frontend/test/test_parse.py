
import os 
import pytest 

from jcompiler.token import tokenize
from jcompiler.parse import Parser

def test_parse_tree(): 
    source = '''
        class Foo { 
            field int x; 
            static char y; 
        }'''
    tokens = tokenize(source) 
    parser = Parser()
    assert parser.parse_tree(tokens) == \
            ['class', 
                ['keyword', 'class'], 
                ['identifier', 'Foo'],
                ['symbol', '{'], 
                ['classVarDec', 
                    ['keyword', 'field'], 
                    ['keyword', 'int'], 
                    ['identifier', 'x'], 
                    ['symbol', ';']], 
                ['classVarDec', 
                    ['keyword', 'static'], 
                    ['keyword', 'char'], 
                    ['identifier', 'y'], 
                    ['symbol', ';']], 
                ['symbol', '}']] 
             

