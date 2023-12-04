def solution(spell, dic):
    res = 0
    for i in dic:
        res = []
        for j in spell:
            if j in i:
                res.append(j)
        if res == spell:
            return 1
            break
    return 2