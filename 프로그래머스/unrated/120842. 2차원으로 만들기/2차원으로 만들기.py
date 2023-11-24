def solution(num_list, n):
    result = []
    while len(num_list) !=0:
        lst = []
        for i in range(0, n):
            num = num_list.pop(0)
            lst.append(num)
        result.append(lst)
    return result
                   
    
    