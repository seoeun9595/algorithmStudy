def solution(number, limit, power):
    res = []
    for i in range(1, number+1):
        prime_num = []
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                prime_num.append(j)
                prime_num.append(i//j)
        len_pn = len(set(prime_num))
        res.append(len_pn if len_pn <= limit else power)
    return sum(res)