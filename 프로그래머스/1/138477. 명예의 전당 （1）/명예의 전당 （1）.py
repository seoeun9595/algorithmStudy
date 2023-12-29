def solution(k, score):
    top = []
    res = []
    for i in score:
        top.append(i)
        top = sorted(top, reverse = True)[:k]
        res.append(min(top))
    return res