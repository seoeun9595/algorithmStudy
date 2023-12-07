def solution(id_pw, db):
    dic = dict(db)
    
    if id_pw[0] not in dic.keys():
        res = "fail"
    else:
        if id_pw[1] == dic[id_pw[0]]:
           res = "login"
        else:
           res = "wrong pw"
    return res