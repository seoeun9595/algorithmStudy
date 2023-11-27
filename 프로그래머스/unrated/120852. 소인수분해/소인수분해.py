def solution(n):
    lst = []
    i = 2
    while n >= i:
        if n % i == 0:
            if i not in lst:
                lst.append(i)      
            n = n // i
        else:
            i += 1
    return lst
        