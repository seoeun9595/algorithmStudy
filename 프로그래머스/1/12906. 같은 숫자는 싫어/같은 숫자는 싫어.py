def solution(arr):
    res = [arr[0]]
    for i in arr:
        if i != res[-1]:
            res.append(i)
    return res