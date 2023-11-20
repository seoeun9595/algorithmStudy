def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    for i in range(1, numer + 1):
        if numer % i == 0 and denom % i == 0:
            cdiv = i
            
    answer = [numer / cdiv, denom / cdiv]
    return answer