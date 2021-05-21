stack = [0]
for i in range(int(input())):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        stack.append(max(nums[1], stack[-1]))
    elif nums[0] == 2:
        stack.pop()
    else:
        print(stack[-1])