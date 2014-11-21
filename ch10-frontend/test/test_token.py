# -*- coding: utf-8 -*- 
# Author    :   Mengyu Zhang (mengyuzhang@uchicago.edu) 
# Date      :   Nov 17 2014 

import os 
import pytest 

from jcompiler.token import tokenize
from jcompiler.token import token_type 

TEST_DIR = os.path.dirname(__file__)

def test_tokenize(): 
    assert ['a'] == tokenize('a')  
    assert ['a', '='] == tokenize('a =')  
    assert ['let', 'a', '=', 'b', ';'] == tokenize('let a = b;')  
    assert tokenize('class Foo { field int a = 404; }') == ['class', 
            'Foo', '{', 'field', 'int', 'a', '=', '404', ';', '}']
    assert tokenize('"hello world."') == ['"hello world."'] 
                    
def test_token_type():
    assert 'integerConstant' == token_type('123') 
    assert 'stringConstant' == token_type('"hello world!"') 
    assert 'identifier' == token_type('foo') 
    assert 'keyword' == token_type('void') 
