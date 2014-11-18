
from jcompiler.tokens import token_stream

class Parser(object): 
    def __init__(self, tokens): 
        self.buf = token_stream(tokens) 
        self.lookahead = self.buf.next() 

