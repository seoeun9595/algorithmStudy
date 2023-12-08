def solution(chicken):
    answer = 0
    while chicken >= 10:
        share = chicken // 10
        remains = chicken % 10
        answer += share
        chicken = share + remains
    return answer