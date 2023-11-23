def solution(numbers, k):
    i = (k * 2 - 1) % len(numbers)
    return numbers[i-1]
