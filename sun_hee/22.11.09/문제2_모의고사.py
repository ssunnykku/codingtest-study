# # 1번 :
# 1, 2, 3, 4, 5
# 1, 2, 3, 4, 5, ...

# # 2번
# 2, 1, 2, 3, 2, 4, 2, 5
# 2, 1, 2, 3, 2, 4, 2, 5

# # 3번
# 3, 3, 1, 1, 2, 2, 4, 4, 5, 5
# 3, 3, 1, 1, 2, 2, 4, 4, 5, 5

# def solution(input):
#     one = [1, 2, 3, 4, 5]
#     two = [2, 1, 2, 3, 2, 4, 2, 5]
#     three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     count_one = 0
#     count_two = 0
#     count_three = 0

#     for i in range(a):
#         for j in range(input):
#             print(i,j)

input = [1, 2, 3, 4, 5]
result = []
one = [1, 2, 3, 4, 5]*2000
two = [2, 1, 2, 3, 2, 4, 2, 5]*1250
three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
count_one = 0
count_two = 0
count_three = 0

for i in range(len(input)):
    if one[i] == input[i]:
        count_one = count_one+1
    if two[i] == input[i]:
        count_two = count_two+1
    if three[i] == input[i]:
        count_three = count_three+1


result.append(max(count_one, count_two, count_three))

print(result)
