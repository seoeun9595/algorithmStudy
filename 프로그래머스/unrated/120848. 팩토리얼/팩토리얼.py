def solution(x):
    i = 2
    while x // i != 0:
        x = x // i
        i += 1
 

    return i - 1
   