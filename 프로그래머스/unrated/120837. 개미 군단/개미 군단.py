def solution(hp):
    lst = [5, 3, 1]
    cnt = 0
    for i in lst:
        cnt += hp // i
        hp = hp % i
    return cnt