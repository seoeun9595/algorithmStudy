def solution(name, yearning, photo):
    dic = dict(zip(name, yearning))
    res = []
    for i in photo:
        tot = 0
        for j in i:
            if j in dic:
                tot += dic[j]
        res.append(tot)
    return res