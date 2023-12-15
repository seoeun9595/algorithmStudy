def solution(a, b):
    tot = [a[i] * b[i] for i in range(len(a))]
    return sum(tot)