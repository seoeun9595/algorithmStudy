def is_prime_number(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(n):
    res = 0
    for i in range(2, n+1):
        if is_prime_number(i) == True:
            res +=1
    return res