def solution(array):
    astr = ""
    for i in array:
        astr = astr + str(i)
    narray = list(astr)
    return len([i for i in narray if i == "7"])