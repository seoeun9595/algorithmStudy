def solution(quiz):
    answer = []
    for i in quiz:
        qlist = i.split()
        n1, n2, n3 = int(qlist[0]), int(qlist[2]), int(qlist[4])
        if qlist[1] == '+':
            res = ("O" if n1 + n2 == n3 else "X")
        else:
            res = res = ("O" if n1 - n2 == n3 else "X")
        answer.append(res)
            
    return answer