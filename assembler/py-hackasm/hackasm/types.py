
from struct import pack

class Word(object): 
    def __init__(self, val=0): 
        self.val = val

    def set_val(self, val): 
        self.val = val 

    def get_vel(self, val): 
        return self.val 

    def to_bytes(self):
        return pack('H', self.val) 

class AInst(object): 
    def __init__(self, imm, symbol_table): 
        self.imm = imm
        self.symbol_table = symbol_table
    
    def to_bytes(self): 
        if isinstance(int, self.imm): 
            val = imm
        else: 
            val = self.symbol_table.query(self.imm) 

        word = Word(val) 
        return word.to_bytes() 

class CInst(object): 
    def __init__(self, comp, dest, jump): 
        comp_map = { 
                '0'     :   0<<6 | 1<<5 | 0<<4 | 1<<3 | 0<<2 | 1<<1 | 0,  
                '1'     :   0<<6 | 1<<5 | 1<<4 | 1<<3 | 1<<2 | 1<<1 | 1, 
                '-1'    :   0<<6 | 1<<5 | 1<<4 | 1<<3 | 0<<2 | 1<<1 | 0, 
                'D'     :   0<<6 | 0<<5 | 0<<4 | 1<<3 | 1<<2 | 0<<1 | 0,  
                'A'     :   0<<6 | 1<<5 | 1<<4 | 0<<3 | 0<<2 | 0<<1 | 0, 
                '!D'    :   0<<6 | 0<<5 | 0<<4 | 1<<3 | 1<<2 | 0<<1 | 1,  
                '!A'    :   0<<6 | 1<<5 | 1<<4 | 0<<3 | 0<<2 | 0<<1 | 1, 
                '-D'    :   0<<6 | 0<<5 | 0<<4 | 1<<3 | 1<<2 | 1<<1 | 1, 
                '-A'    :   0<<6 | 1<<5 | 1<<4 | 0<<3 | 0<<2 | 1<<1 | 1,  
                'D+1'   :   0<<6 | 0<<5 | 1<<4 | 1<<3 | 1<<2 | 1<<1 | 1,  
                'A+1'   :   0<<6 | 1<<5 | 1<<4 | 0<<3 | 1<<2 | 1<<1 | 1, 
                'D-1'   :   0<<6 | 0<<5 | 0<<4 | 1<<3 | 1<<2 | 1<<1 | 0, 
                'A-1'   :   0<<6 | 1<<5 | 1<<4 | 0<<3 | 0<<2 | 1<<1 | 0,  
                'D+A'   :   0<<6 | 0<<5 | 0<<4 | 0<<3 | 0<<2 | 1<<1 | 0,  
                'D-A'   :   0<<6 | 0<<5 | 1<<4 | 0<<3 | 0<<2 | 1<<1 | 1,  
                'A-D'   :   0<<6 | 0<<5 | 0<<4 | 0<<3 | 1<<2 | 1<<1 | 1, 
                'D&A'   :   0<<6 | 0<<5 | 0<<4 | 0<<3 | 0<<2 | 0<<1 | 0, 
                'D|A'   :   0<<6 | 0<<5 | 1<<4 | 0<<3 | 1<<2 | 0<<1 | 1,  
                'M'     :   1<<6 | 1<<5 | 1<<4 | 0<<3 | 0<<2 | 0<<1 | 0,  
                '!M'    :   1<<6 | 1<<5 | 1<<4 | 0<<3 | 0<<2 | 0<<1 | 1,  
                '-M'    :   1<<6 | 1<<5 | 1<<4 | 0<<3 | 0<<2 | 1<<1 | 1,  
                'M+1'   :   1<<6 | 1<<5 | 1<<4 | 0<<3 | 1<<2 | 1<<1 | 1,  
                'M-1'   :   1<<6 | 1<<5 | 1<<4 | 0<<3 | 0<<2 | 1<<1 | 0,  
                'D+M'   :   1<<6 | 0<<5 | 0<<4 | 0<<3 | 0<<2 | 1<<1 | 0,  
                'D-M'   :   1<<6 | 0<<5 | 1<<4 | 0<<3 | 0<<2 | 1<<1 | 1,  
                'M-D'   :   1<<6 | 0<<5 | 0<<4 | 0<<3 | 1<<2 | 1<<1 | 1, 
                'D&M'   :   1<<6 | 0<<5 | 0<<4 | 0<<3 | 0<<2 | 0<<1 | 0, 
                'D|M'   :   1<<6 | 0<<5 | 1<<4 | 0<<3 | 1<<2 | 0<<1 | 1,  

                }
        dest_map = {
                'null'  :   0<<2 | 0<<1 | 0, 
                'M'     :   0<<2 | 0<<1 | 1, 
                'D'     :   0<<2 | 1<<1 | 0, 
                'MD'    :   0<<2 | 1<<1 | 1, 
                'A'     :   1<<2 | 0<<1 | 0, 
                'AM'    :   1<<2 | 0<<1 | 1,
                'AD'    :   1<<2 | 1<<1 | 0, 
                'AMD'   :   1<<2 | 1<<1 | 1, 
                }
        jump_map = { 
                'null'  :   0<<2 | 0<<1 | 0, 
                'JGT'   :   0<<2 | 0<<1 | 1, 
                'JEQ'   :   0<<2 | 1<<1 | 0, 
                'JGE'   :   0<<2 | 1<<1 | 1, 
                'JLT'   :   1<<2 | 0<<1 | 0, 
                'JNE'   :   1<<2 | 0<<1 | 1, 
                'JLE'   :   1<<2 | 1<<1 | 0, 
                'JMP'   :   1<<2 | 1<<1 | 1, 
                }
        self.comp_val = comp_map[comp] 
        self.dest_val = dest_map[dest] 
        self.jump_val = jump_map[jump] 

    def to_bytes(self): 
        val = 1<<15 | 1<<14 | 1<<13
        val |= self.comp_val << 6; 
        val |= self.dest_val << 3; 
        val |= self.jump_val << 0; 

        word = Word() 
        word.set_val(val) 
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

