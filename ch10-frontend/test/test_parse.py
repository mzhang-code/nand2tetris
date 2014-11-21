
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
    parser = Parser(tokens)
    assert parser.parse_tree() == \
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
    parser = Parser(tokens)
    assert parser.parse_tree() == \
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

    
def test_if_stmt(): 
    source = ''' 
        if (x > 0) { 
            let y = x + 1; 
        }'''
    tokens = tokenize(source) 
    parser = Parser(tokens)

    assert parser.if_stmt() == \
            ['ifStatement', 
                ['keyword', 'if'], 
                ['symbol', '('], 
                ['expression', 
                    ['term', 
                        ['identifier', 'x']], 
                    ['symbol', '>'], 
                    ['term', 
                        ['integerConstant', '0']]], 
                ['symbol', ')'], 
                ['symbol', '{'], 
                ['statements', 
                    ['letStatement', 
                        ['keyword', 'let'], 
                        ['identifier', 'y'], 
                        ['symbol', '='], 
                        ['expression', 
                            ['term', 
                                ['identifier', 'x']], 
                            ['symbol', '+'], 
                            ['term', 
                                ['integerConstant', '1']]], 
                        ['symbol', ';']]], 
                ['symbol', '}']] 


def test_let_stmt(): 
    source = 'let square = Square.new(0, 0, 30);' 
    tokens = tokenize(source) 
    parser = Parser(tokens)

    print parser.let_stmt() 

