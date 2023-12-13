def solution(arr, divisor):
    arr = sorted(arr)
    res = [i for i in arr if i % divisor == 0]
    return ([-1] if len(res) == 0 else res)