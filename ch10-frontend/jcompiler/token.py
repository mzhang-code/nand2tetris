
import re 
import sys 

keywords = ['class', 'constructor', 'function', 'method', 'field', 
        'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 
        'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 
        'return'] 

symbols = [r'\{', r'\}', r'\(', r'\)', r'\[', r'\]', 
        r'\.', ',', ';', r'\+', r'\-', r'\*', '/', '&', 
        r'\|', r'\<', r'\>', r'\=', '~'] 

integers = [r'\d+'] 

strings = [r'"[^"]"'] 

ids = [r'[a-zA-Z_]\w*'] 

def tokenize(s): 
    pattern = '|'.join(keywords + symbols + integers + strings + ids) 
    return re.findall(pattern, s)

def token_type(t): 
    if t in keywords: 
        return 'keyword' 
    elif t in '{}()[].,;+-*/&|<>=~': 
        return 'symbol' 
    elif t.startswith('"') and t.endswith('"'): 
        return 'stringConstant'
    else: 
        try: 
            int(t) 
            return 'integerConstant' 
        except ValueError as e: 
            return 'identifier' 

def token_stream(tokens): 
    for t in tokens: 
        yield t
    yield '$' 

