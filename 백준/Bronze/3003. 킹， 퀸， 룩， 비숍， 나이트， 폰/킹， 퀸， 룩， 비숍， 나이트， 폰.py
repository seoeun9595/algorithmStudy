correct = [1, 1, 2, 2, 2, 8]
input_nums = list(map(int, input().split()))

for i in range(len(correct)):
    print(correct[i] - input_nums[i], end = ' ')
