def solution(lines):
    sorted_lines = sorted(lines)
    min_val = min(map(min, sorted_lines))
    max_val = max(map(max, sorted_lines))
    key = [i for i in range(min_val, max_val)]
    item = [0 for i in range(max_val - min_val)]
    cnt = dict(zip(key, item))
    
    for i in sorted_lines:
        for j in range(i[0], i[1]):
            if j in cnt:
                cnt[j] = cnt[j] + 1

    res = 0
    for i in cnt.values():
        if i > 1:
            res += 1
    return res