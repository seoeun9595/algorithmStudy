def solution(s):
    sets = set(s)
    res = ''
    for i in sets:
        if s.count(i) == 1:
            res = res + i
    return "".join(sorted(res))