def solution(numbers):
    tot = sum([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    hap = 0
    for i in numbers:
        hap += i
    return (tot - hap)