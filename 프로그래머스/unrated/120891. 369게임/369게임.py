def solution(order):
    s = str(order)
    lst = ['3', '6', '9']
    cnt = 0
    for i in s:
        if i in lst:
            cnt += 1
    return cnt