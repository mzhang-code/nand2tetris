
import pytest 

from hackasm.parser import Parser

def test_preprocess(): 
    parser = Parser() 
    lines = ['', 
             '\n', 
             '\\\\ starts :-) \n', 
             '@1024\n', 
             'MD    = M + 1 \\\\ inc M, and set the val to D! \n', 
             '(LOOP   )\n'] 

    l1, l2, l3 = parser.preprocess(lines) 
    assert l1 == '@1024' 
    assert l2 == 'MD=M+1' 
    assert l3 == '(LOOP)' 

