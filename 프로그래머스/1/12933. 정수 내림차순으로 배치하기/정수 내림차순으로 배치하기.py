def solution(n):
    num = sorted([i for i in str(n)], reverse = True)
    res = "".join(num)
    return int(res)