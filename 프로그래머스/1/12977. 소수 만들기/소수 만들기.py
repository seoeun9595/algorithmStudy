def is_prime_number(num):
    divisor = [i for i in range(1, num+1) if num % i == 0]
    return True if len(divisor) == 2 else False

def solution(nums):
    len_nums = len(nums)
    res = 0
    for i in range(0, len_nums-2):
        for j in range(i+1, len_nums-1):
            for k in range(j+1, len_nums):
                if is_prime_number(nums[i] + nums[j] + nums[k]):
                    res += 1
    return res