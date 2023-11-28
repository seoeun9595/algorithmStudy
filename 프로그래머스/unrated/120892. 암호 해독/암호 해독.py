def solution(cipher, code):
    str = ""
    for i in range(0, len(cipher)):
        if i % code == code - 1:
            str = str + cipher[i]
    return str
        