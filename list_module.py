'''
def List_caller(j):
    a = []
    b = []
    c = []
    for i in j:
        if type(i) == str:
            a.append(i)
        if type(i) == float or type(i) == int:
            b.append(i)
        if type(i) == bool:
            c.append(i)
    if len(a) == 0 and len(c) == 0 and len(b) != 0:
        return b
    elif len(a) == 0 and len(c) != 0 and len(b) == 0:
        return c
    elif len(a) != 0 and len(c) == 0 and len(b) == 0:
        return a
    elif len(a) == 0 and len(c) != 0 and len(b) != 0:
        return b, c
    elif len(a) != 0 and len(c) == 0 and len(b) != 0:
        return a, b 
    elif len(a) != 0 and len(c) != 0 and len(b) == 0:
        return a, c
    return a, b, c
'''
def List_math(k,l):
    for i in l:
        if k % i == 0:
            return False
    return True



