def solution(my_string, num1, num2):
    s1 = my_string[num1]
    s2 = my_string[num2]
    res = ''
    
    for i in range(0, len(my_string)):
        if i == num1:
            res = res + s2
        elif i == num2:
            res = res + s1
        else:
            res = res + my_string[i]
    return res