def solution(s, n):
    res = ""
    for i in s:
        if i.islower():
            res += chr((ord(i) + n) % 123 % 97 + 97)
        elif i.isupper():
            res += chr((ord(i) + n) % 91 % 65 + 65)
        else:
            res += i
    return res