def solution(age):
    result = ""
    for i in str(age):
        result += chr(ord(i) + 49)
        
    return result
        