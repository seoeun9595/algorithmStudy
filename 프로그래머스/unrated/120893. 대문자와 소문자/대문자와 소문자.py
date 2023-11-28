def solution(my_string):
    res = ''
    for i in my_string:
        if i.isupper() == True:
            res = res + i.lower()
        else:
            res = res + i.upper()
    return res