def solution(my_string):
    slist = my_string.split()
    
    while len(slist) > 1:
        n1, op, n2 = int(slist.pop(0)), slist.pop(0), int(slist.pop(0))
        res = (n1 + n2 if op == '+' else n1 - n2)
        slist.insert(0, res)
    return res
    