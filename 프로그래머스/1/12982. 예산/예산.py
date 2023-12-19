def solution(d, budget):
    d.sort()
    res = 0
    for i in d:
        budget -= i
        if budget < 0:
            break
        res += 1
    return res