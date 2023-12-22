def solution(s):
    dic = {}
    res = []
    
    for i in s:
        if i not in dic:
            res.append(-1)
            dic[i] = s.index(i)
            s = s.replace(i, "-", 1)
        else:
            res.append(s.index(i)-dic[i])
            dic[i] = s.index(i)
            s = s.replace(i, "-", 1)
    return res