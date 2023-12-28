def solution(a, b, n):
    answer = 0
    while n >= a:
        share = n // a
        remains = n % a
        answer += share * b
        n = share * b + remains
    return answer