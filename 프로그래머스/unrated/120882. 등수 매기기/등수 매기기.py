def solution(score):
    mean = [(i[0] + i[1]) / 2 for i in score]
    s_mean = sorted(mean, reverse = True)
    res = [s_mean.index(i) + 1 for i in mean]
    return res
        