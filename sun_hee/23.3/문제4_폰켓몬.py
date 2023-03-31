nums = [3,3,3,2,2,4]

n = len(nums)//2

set_list = list(set(nums))

if len(set_list) >= n:
    print(n)
else:
    print(len(set_list))
