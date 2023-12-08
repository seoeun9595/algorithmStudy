def solution(i, j, k):
    mstr = ""
    for num in range(i, j+1):
        mstr = mstr + str(num)
    return mstr.count(str(k))