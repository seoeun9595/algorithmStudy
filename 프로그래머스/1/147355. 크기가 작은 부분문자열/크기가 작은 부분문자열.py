def solution(t, p):
    lenT = len(t)
    lenP = len(p)
    cnt = 0
    for i in range(lenT - lenP + 1):
        if int(t[i:i+lenP]) <= int(p):
            cnt += 1
    return cnt