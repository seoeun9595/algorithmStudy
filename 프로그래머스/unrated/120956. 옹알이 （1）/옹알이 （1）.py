def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for i in babbling:
        for j in can:
            i = i.replace(j, "1")
        if i.isdigit():
            cnt += 1
    return cnt