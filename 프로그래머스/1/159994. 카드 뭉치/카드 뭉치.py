def solution(cards1, cards2, goal):
    res = []
    i, j = 0, 0
    
    for word in goal:
        if i < len(cards1) and word == cards1[i]:
            res.append(cards1[i])
            i += 1
        if j < len(cards2) and word == cards2[j]:
            res.append(cards2[j])
            j += 1
            
    return "Yes" if res == goal else "No"