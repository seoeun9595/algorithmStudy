def gcd(a, b):
    res = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            res = i
    return res

def solution(a, b):
    b_gcd = gcd(a, b)
    b = b // b_gcd
    
    while b % 2 == 0:
        b = b // 2
    while b % 5 == 0:
        b = b // 5
    return (1 if b == 1 else 2)