def solution(strings, n):
    strings.sort()
    dic = {}
    for i in strings:
        dic[i] = i[n]
    s_dic = sorted(dic.items(), key= lambda item:item[1])
    return [i[0] for i in s_dic]