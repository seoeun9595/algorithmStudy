def solution(s):
    s_list = s.split(" ")
    answer = [i.capitalize() for i in s_list]
    return " ".join(answer)