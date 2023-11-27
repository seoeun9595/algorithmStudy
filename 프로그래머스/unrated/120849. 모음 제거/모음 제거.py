def solution(my_string):
    result = ''
    lst = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in lst:
            result += i
    return result