def solution(array):
    array.sort()
    if len(array) % 2 == 0:
        return (array[len(array) // 2 - 1] + array[len(array) // 2]) / 2
    else:
        return array[len(array) // 2]
    answer = 0
    return answer