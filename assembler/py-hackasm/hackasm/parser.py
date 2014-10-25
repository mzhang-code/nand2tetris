
import re 
from hackasm.types import AInst 
from hackasm.types import CInst 
from hackasm.types import SymbolTable 

class Parser(object): 
    def __init__(self): 
        self.symbol_table = None

    def preprocess(self, lines): 
        remove_spaces = lambda l: re.sub(r'\s+', '', l.strip())
        remove_comments = lambda l: re.sub(r'\\{2}\S+', '', l)
        exprs = map(remove_spaces, lines) 
        exprs = map(remove_comments, exprs) 
        return filter(lambda l: l, exprs) 

    def parse(self, lines): 
        self.symbol_table = SymbolTable() 
        exprs = self.preprocess(lines) 
        exprs = self.remove_labels(exprs) 
        insts = map(self.gen_inst, exprs) 
        return ''.join(map(lambda inst: inst.to_bytes(), insts)) 

    def is_a_inst(self, expr): 
        return '@' in expr 

    def is_label(self, expr): 
        return expr.startswith('(') and expr.endswith(')') and expr[1:-1]

    def is_c_inst(self, expr): 
        return not (self.is_a_inst(expr) or self.is_label(expr)) 

    def remove_labels(self, exprs): 
        inst_cnt = 0 
        for e in exprs: 
            if self.is_label(e): 
                symbol_table.insert(e[1:-1], inst_cnt) 
            else: 
                inst_cnt += 1 
        return filter(lambda e: not self.is_label(e), exprs) 

    def gen_inst(self, expr): 
        if self.is_a_inst(expr): 
            try:
                addr = int(expr[1:]) 
            except ValueError as e: 
                addr = expr[1:] 
            return AInst(addr, self.symbol_table) 

        if self.is_c_inst(expr): 
            jump = 'null' 
            if ';' in expr: 
                jump = expr[expr.index(';')+1;] 
                expr = expr[:expr.index(';')] 

            dest = 'null' 
            comp = expr
            if '=' in expr: 
                dest = expr[:expr.index('=')] 
                comp = expr[expr.index('=')+1:] 
            return CInst(comp, dest, jump) 

        raise ValueError("Unknown Instruntion Type for %s" %expr) 

