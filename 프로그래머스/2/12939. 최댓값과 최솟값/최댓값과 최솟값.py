def solution(s):
    s_list = s.split()
    s_list = [int(i) for i in s_list]
    answer = str(min(s_list)) + " " + str(max(s_list))
    return answer