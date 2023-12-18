def solution(n):
    nstr = ''
    while n > 0:
        n, mod = divmod(n, 3)
        nstr += str(mod)
    return int(nstr, 3)