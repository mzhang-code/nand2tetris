
import re 
import sys 

keywords = ['class', 'constructor', 'function', 'method', 'field', 
        'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 
        'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 
        'return'] 

symbols = [r'\{', r'\}', r'\(', r'\)', r'\[', r'\]', 
        r'\.', ',', ';', r'\+', r'\-', r'\*', '/', '&', 
        r'\|', r'\<', r'\>', r'\=', '~'] 

intgers = [r'\d+'] 

strings = [r'"[^"]"'] 

ids = [r'^[^\d\W]\w*'] 

def tokenize(s): 
    pattern = '|'.join(keywords + symbols + intgers + strings + ids) 
    return re.findall(pattern, s)

