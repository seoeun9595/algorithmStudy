def solution(absolutes, signs):
    tot = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            tot += absolutes[i]
        else:
            tot += -absolutes[i]
    return tot