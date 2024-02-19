def solution(s):
    cvt_cnt = 0
    zero_cnt = 0
    
    while s != "1":
        zero_cnt += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        cvt_cnt += 1
        
    return [cvt_cnt, zero_cnt]