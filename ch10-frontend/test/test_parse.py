
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
             
    source = '''
        class Foo { 
            field int x; 
            static char y; 

            method void bar(int a, int b) { 
                return; 
            }
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
                ['subroutineDec', 
                    ['keyword', 'method'], 
                    ['keyword', 'void'], 
                    ['identifier', 'bar'], 
                    ['symbol', '('], 
                    ['parameterList', 
                        ['keyword', 'int'], 
                        ['identifier', 'a'], 
                        ['symbol', ','], 
                        ['keyword', 'int'], 
                        ['identifier', 'b']], 
                    ['symbol', ')'], 
                    ['subroutineBody', 
                        ['symbol', '{'], 
                        ['statements', 
                            ['returnStatement', 
                                ['keyword', 'return'], 
                                ['symbol', ';']]], 
                        ['symbol', '}']]], 
                ['symbol', '}']] 

