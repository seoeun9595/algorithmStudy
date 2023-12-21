def solution(sizes):
    for i in sizes:
        i.sort()
    one = [i[0] for i in sizes]
    two = [i[1] for i in sizes]
    return max(one) * max(two)