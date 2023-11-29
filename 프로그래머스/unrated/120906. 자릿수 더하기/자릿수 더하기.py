def solution(n):
    nlist = list(str(n))
    tot = 0
    for i in nlist:
        tot = tot + int(i)
    return tot
    