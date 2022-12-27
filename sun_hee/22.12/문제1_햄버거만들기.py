

# 1번째 시도
# 1 빵 2 야채 3 고기
# 빵 야채 고기 빵 1, 2, 3, 1
# ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
# ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
# answer = 0

# 시간초과남
# def solution(ingredient):
#     answer = 0
#     while len(ingredient) >= 4:
#         for i in range(len(ingredient)):
#             if ingredient[i:i+4] != [1, 2, 3, 1]:
#                 answer += 0
#             if ingredient[i:i+4] == [1, 2, 3, 1]:
#                 del ingredient[i:i+4]
#                 answer += 1
#         if answer == 0 or len(ingredient) < 4:
#             break
#     return answer


# 다른 사람의 풀이
ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]


def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cnt


print(solution(ingredient))

# 다시 시도

# ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
# answer = 0

# new = [i for i in ingredient]

# if new[-4] == [1, 2, 3, 1]:
#     answer += 1
#     new.pop()
# print(new)
# print(answer)
