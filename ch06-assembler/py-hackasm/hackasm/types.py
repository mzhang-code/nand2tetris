
from struct import pack

WORD_LEN = 16

class Word(object): 
    def __init__(self, buf='0'*WORD_LEN): 
        self.buf = buf

    def set_val(self, val): 
        buf = '' 
        while val: 
            if val % 2: 
                buf += '1' 
            else: 
                buf += '0' 
            val /= 2
        self.buf = buf[:WORD_LEN][::-1] 

    def get_val(self): 
        val = 0
        for b in self.buf: 
            val = val << 1 
            val += int(b)
        return val 

    def to_bytes(self):
        return self.buf.zfill(WORD_LEN)

class AInst(object): 
    def __init__(self, imm, symbol_table): 
        self.imm = imm
        self.symbol_table = symbol_table
    
    def to_bytes(self): 
        if isinstance(self.imm, int): 
            val = self.imm
        else: 
            val = self.symbol_table.query(self.imm) 

        word = Word() 
        word.set_val(val)
        return word.to_bytes() 

class CInst(object): 
    def __init__(self, comp, dest, jump): 
        comp_map = { 
                '0'     :  '0101010',  
                '1'     :  '0111111', 
                '-1'    :  '0111010', 
                'D'     :  '0001100',  
                'A'     :  '0110000', 
                '!D'    :  '0001101',  
                '!A'    :  '0110001', 
                '-D'    :  '0001111', 
                '-A'    :  '0110011',  
                'D+1'   :  '0011111',  
                'A+1'   :  '0110111', 
                'D-1'   :  '0001110', 
                'A-1'   :  '0110010',  
                'D+A'   :  '0000010',  
                'D-A'   :  '0010011',  
                'A-D'   :  '0000111', 
                'D&A'   :  '0000000', 
                'D|A'   :  '0010101',  
                'M'     :  '1110000',  
                '!M'    :  '1110001',  
                '-M'    :  '1110011',  
                'M+1'   :  '1110111',  
                'M-1'   :  '1110010',  
                'D+M'   :  '1000010',  
                'D-M'   :  '1010011',  
                'M-D'   :  '1000111', 
                'D&M'   :  '1000000', 
                'D|M'   :  '1010101',  

                }
        dest_map = {
                'null'  :   '000', 
                'M'     :   '001', 
                'D'     :   '010', 
                'MD'    :   '011', 
                'A'     :   '100', 
                'AM'    :   '101',
                'AD'    :   '110', 
                'AMD'   :   '111', 
                }
        jump_map = { 
                'null'  :   '000', 
                'JGT'   :   '001', 
                'JEQ'   :   '010', 
                'JGE'   :   '011', 
                'JLT'   :   '100', 
                'JNE'   :   '101', 
                'JLE'   :   '110', 
                'JMP'   :   '111', 
                }
        self.comp_val = comp_map[comp] 
        self.dest_val = dest_map[dest] 
        self.jump_val = jump_map[jump] 

    def to_bytes(self): 
        word = Word('111' + self.comp_val + self.dest_val + self.jump_val) 
        return word.to_bytes() 

class SymbolTable(object): 
    def __init__(self): 
        self.table = {} 
        self.alloc_addr = 16

    def insert(self, symbol, addr): 
        if addr: 
            self.table[symbol] = addr
            return addr 

        self.table[symbol] = self.alloc_addr 
        self.alloc_addr += 1 
        return self.table[symbol] 

    def query(self, symbol): 
        if symbol in self.table: 
            return self.table[symbol]
        
        return self.insert(symbol, None) 

