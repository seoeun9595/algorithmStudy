def cnt(num):
    res = [i for i in range(1, num+1) if num % i == 0]
    return len(res)

def solution(left, right):
    tot = 0
    for i in range(left, right + 1):
        if cnt(i) % 2 == 0:
            tot += i
        else:
            tot -= i
    return tot