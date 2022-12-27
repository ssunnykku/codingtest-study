

# 1번 시도
# 1 빵 2 야채 3 고기
# 빵 야채 고기 빵 1, 2, 3, 1
# ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
# ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
answer = 0


# while len(ingredient) > 4:
#     for i in range(len(ingredient)):
#         if ingredient[i:i+4] == [1, 2, 3, 1]:
#             del ingredient[i:i+4]
#             answer += 1
#         else:
#             answer += 0

# print(answer)

# def hamburg(ingredient):
#     answer = 0
#     return answer


# 222222
# ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
# answer = 0

new = []
# # while len(ingredient) > 4:
# for i in range(len(ingredient)):
#     new.append(ingredient[i:i+4])
#     # del ingredient[i:i+4]
#     # answer += 1
#     # break
# # print(new)
ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
new = [ingredient[i:i+4] for i in range(len(ingredient))]
for i in range(len(ingredient)):
    if ingredient[i:i+4] != [1, 2, 3, 1]:
        answer += 0
else:
    while len(ingredient) > 4:
        for i in range(len(ingredient)):
            if ingredient[i:i+4] == [1, 2, 3, 1]:
                del ingredient[i:i+4]
                answer += 1

# print(answer)


def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cnt


print(solution(ingredient))
