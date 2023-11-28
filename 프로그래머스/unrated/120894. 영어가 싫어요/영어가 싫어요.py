def solution(numbers):
    dic = {'zero' : 0, 'one':1, 'two':2, 'three' : 3, 'four':4,
           'five':5,'six' : 6, 'seven' : 7, 'eight':8,'nine':9}

    nstr = ''
    lst = []

    numList = list(numbers)
    while len(numList) != 0:
        while nstr not in dic.keys():
            nstr = nstr + numList.pop(0)
        lst.append(nstr)
        nstr = ''

    res = []
    for i in lst:
        for k, v in dic.items():
            if i == k:
                res.append(str(v))
    result = "".join(res)

    return int(result)