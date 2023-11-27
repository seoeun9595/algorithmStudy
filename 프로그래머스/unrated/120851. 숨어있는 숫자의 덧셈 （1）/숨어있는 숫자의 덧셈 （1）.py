def solution(my_string):
    lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = []
    for i in my_string:
        if i in lst:
            result.append(int(i))
    return sum(result)