
from jcompiler.token import token_stream

class Parser(object): 
    def __init__(self): 
        self.buf = '' 
        self.lookahead = '' 

    def match(self, t): 
        self.lookahead = self.buf.next() 

    def parse_tree(self, tokens): 
        self.buf = token_stream(tokens) 
        self.lookahead = self.buf.next() 
        return self.klass() 

    def pack_node(self, *args): 
        return list(args) 

    def klass(self): 
        if self.lookahead == 'class': 
            return ['class', self.keyword(), self.class_name(), 
                    self.symbol()] + self.class_vars() + \
                    self.subroutines() + [self.symbol()] 
        else: 
            pass 

    def keyword(self): 
        t = self.lookahead 
        self.match(t) 
        return ['keyword', t]

    def identifier(self): 
        t = self.lookahead
        self.match(t) 
        return ['identifier', t] 

    def symbol(self): 
        t = self.lookahead 
        self.match(t) 
        return ['symbol', t] 

    def class_vars(self): 
        if self.lookahead not in ['static', 'field']: 
            return []
        return [['classVarDec', self.keyword(), self.type(), 
            self.var_name()] + self.var_names() + [self.symbol()]] + \
            self.class_vars()

    def type(self): 
        t = self.lookahead
        self.match(t) 
        if t in ['int', 'char', 'boolean']: 
            return ['keyword', t] 
        else: 
            return ['identifier', t] 

    def class_name(self): 
        return self.identifier() 

    def var_name(self): 
        return self.identifier() 

    def subroutine_name(self): 
        return self.identifier() 

    def var_names(self): 
        '''zero or more var names'''
        t = self.lookahead
        if t == ',': 
            return [self.symbol(), self.var_name()] + sef.var_names()
        else: 
            return [] 

    def subroutines(self): 
        if self.lookahead not in ['constructor', 'function', 'method']: 
            return [] 
        return [['subroutineDec', self.keyword(), self.ret_type(), 
            self.subroutine_name(), self.symbol(), self.para_list(), 
            self.symbol(), self.subroutine_body()]] + self.subroutines() 

    def subroutine_body(self): 
        return 'BODY' 

