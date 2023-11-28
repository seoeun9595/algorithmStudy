def solution(num, k):
    nlist = list(str(num))
    if str(k) in nlist:
        return nlist.index(str(k)) + 1
    else:
        return -1