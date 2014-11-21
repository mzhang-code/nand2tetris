
def convert_special_char(c): 
    D = {'<': '&lt', '>': '&gt'} 
    if c in D.keys(): 
        return D[c] 
    return c 

def dump_parse_tree(root, level=0, pretty=True): 
    if pretty: 
        TAB = level * '\t' 
        NL = '\n' 
    else: 
        TAB = '' 
        NL = '' 

    # empty node
    if not root[1]: 
        return TAB + '<%s> </%s>' %(root[0], root[0]) + NL 

    # leaf node 
    if not isinstance(root[1], list):
        return TAB + '<%s> %s </%s>' %(root[0], 
                convert_special_char(root[1]), root[0]) + NL 

    # interior node 
    res = TAB + '<%s>' % root[0] + NL 
    for node in root[1:]:
        res += dump_parse_tree(node, level + 1) 

    return res + TAB + '</%s>' % root[0] + NL 

