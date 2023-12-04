def solution(sides):
    n1 = sum(sides) - max(sides)
    n2 = max(sides) - (max(sides) - min(sides) + 1)
    return n1 + n2