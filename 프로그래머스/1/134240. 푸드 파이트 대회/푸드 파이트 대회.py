def solution(food):
    res = ["0"]
    rep = [i // 2 for i in food[1:]]
    for i in range(len(rep), 0, -1):
        for j in range(rep[i-1]):
            res.insert(0, str(i))
            res.append(str(i))
    return "".join(res)