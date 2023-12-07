def solution(numlist, n):
    s_numlist = sorted(numlist, reverse = True)
    lst = [abs(i - n) for i in s_numlist]
    
    dic = dict(zip(s_numlist, lst))
    s_dic = sorted(dic.items(), key = lambda item: item[1])
    res = [i[0] for i in s_dic]
    return res