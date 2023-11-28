def solution(array, n):
    array.sort()
    sres = 100
    res = 0
    for i in array:
        if abs(i - n) < sres:
            sres = abs(i - n)
            res = i
    return res
        