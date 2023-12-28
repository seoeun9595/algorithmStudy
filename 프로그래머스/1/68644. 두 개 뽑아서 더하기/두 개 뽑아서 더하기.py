def solution(numbers):
    res = []
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            res.append(numbers[i] + numbers[j])
    return sorted(list(set(res)))