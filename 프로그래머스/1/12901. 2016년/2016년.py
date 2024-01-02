def solution(a, b):
    dic = {0: "FRI", 1: "SAT", 2: "SUN", 3: "MON", 4: "TUE", 5: "WED", 6: "THU"}
    day = 0
    for i in range(1, a):
        if i == 2:
            day += 29
        elif i in [1, 3, 5, 7, 8, 10, 12]:
            day += 31
        else:
            day += 30
    day += b-1
    return dic[day % 7]