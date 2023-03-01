nums = list(map(int, input()))

# nums.sort()
result = 0
# 0 1 더해주고
# 그 외에는 곱해준다
for i in range(len(nums)):
    if nums[i] <= 1 or result <= 1:
        result += nums[i]
    elif nums[i] > 0:
        result *= nums[i]
print(result)
