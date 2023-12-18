def solution(n, m):
    gcd = max([i for i in range(1, min(n, m) + 1) if n % i == 0 and m % i == 0])
    return [gcd, n * m / gcd]