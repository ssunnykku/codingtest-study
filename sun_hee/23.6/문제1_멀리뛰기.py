# https://school.programmers.co.kr/learn/courses/30/lessons/12914
# 3월 실패 후 재도전
# 피보나치

# 실패 : 시간초과 (모든 경우의 수 다 구해본 코드)
# def solution(n):
#     answer = 0

#     d = [[0, 0]]

#     d[0][0] += 1
#     d[0][1] += 2

#     for i in range(1, n + 1):
#         d.append([0] * len(d[i - 1]) * 2)
#         for j in range(len(d[i])):
#             if j % 2 == 0:
#                 d[i][j] = d[i - 1][j // 2] + 1
#             else:
#                 d[i][j] = d[i - 1][j // 2] + 2
#         answer += d[i-1].count(n)

#     return answer%1234567

n = 2


def solution(n):
    d = [0] * n
    if n == 1:
        return 1
    elif n >= 2:
        d[0], d[1] = 1, 2
    else:
        return 0
    for i in range(2, n):
        d[i] += d[i - 1] + d[i - 2]

    answer = d[-1]

    return answer % 1234567


print(solution(n))
