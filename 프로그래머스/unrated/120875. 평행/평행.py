def calc(dot1, dot2):
    return (dot2[1] - dot1[1]) / (dot2[0] - dot1[0]) 

def solution(dots):
    res = 0
    if calc(dots[0], dots[1]) == calc(dots[2], dots[3]):
        res =  1
    elif calc(dots[0], dots[2]) == calc(dots[1], dots[3]):
        res =  1
    elif calc(dots[0], dots[3]) == calc(dots[1], dots[2]):
        res = 1
    else:
        res = 0
    return res