def solution(k, m, score):
    s = sorted(score, reverse = True)
    res = [s[i*m:(i+1)*m] for i in range(0, (len(score)+1)//m)]
    
    tot = 0
    for i in res:
        if len(i) == m:
            tot += min(i)*m
    return tot