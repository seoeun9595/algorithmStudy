def solution(before, after):
    for i in before:
        after = after.replace(i, "", 1)
    return (1 if len(after) == 0 else 0)