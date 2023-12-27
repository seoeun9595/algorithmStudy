def solution(n, arr1, arr2):
    aLen = len(arr1)
    b_arr1 = [format(i, "b") for i in arr1]
    b_arr2 = [format(i, "b") for i in arr2]
    
    for i in range(aLen):
        while len(b_arr1[i]) < aLen:
            b_arr1[i] = "0" + b_arr1[i]

    for i in range(aLen):
        while len(b_arr2[i]) < aLen:
            b_arr2[i] = "0" + b_arr2[i]
            
    res = []
    for i in range(aLen):
        line = ""
        for j in range(aLen):
            if b_arr1[i][j] == "0" and b_arr2[i][j] == "0":
                line += " "
            else:
                line += "#"
        res.append(line)
    return res