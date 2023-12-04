def solution(polynomial):
    lst = polynomial.split(" + ")
    x = [i for i in lst if "x" in i]
    num = [i for i in lst if "x" not in i]
    
    numsum = str(sum([int(i) for i in num]))
        
    xsum = 0
    for i in x:
        if len(i) > 1:
            xsum += int(i[:-1]) 
        elif len(i) == 1:
            xsum += 1   
                                   
    xstr = str(xsum)

    if xstr == "0":
        return numsum
    elif xstr == "1":
        if numsum == "0":
            return ("x")
        else:
            return ("x + " + numsum)
    else:
        if numsum == "0":
            return (xstr + "x")
        else:
            return (xstr + "x + " + numsum)