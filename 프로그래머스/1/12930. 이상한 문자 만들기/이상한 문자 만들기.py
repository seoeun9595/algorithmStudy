def solution(s):
    word = s.split(' ')
    res = ''
    for i in word:
        word_i = ''
        for j in range(len(i)):
            if j % 2 == 0:
                res += i[j].upper()
            else:
                res += i[j].lower()
        res += ' '
    return res[:-1]