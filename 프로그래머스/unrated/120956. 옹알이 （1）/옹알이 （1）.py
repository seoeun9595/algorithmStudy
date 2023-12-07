def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for i in babbling:
        for j in can:
            i = i.replace(j, " ")
        i = i.replace(" ", "")
        if len(i) == 0:
            cnt += 1
    return cnt