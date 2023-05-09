# https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3

# 가격이 떨어지지 않은 기간이 몇 초인지 리턴
from collections import deque


# 현재 숫자 이후 탐색
# 만약 현재 숫자보다 크다면 +1?


# def solution(prices):
#     d = deque(prices)
#     answer = []
#     for i in range(len(prices)):
#         cnt = 0
#         for j in list(d)[1:]:
#             if j >= list(d)[0]:
#                 cnt += 1
#             else:
#                 break
#         if cnt == 0:
#             answer.append(1)
#         else:
#             answer.append(cnt)

#         d.popleft()
#     answer[-1] = 0
#     return answer

# 실패!!!!!! 테스트 코드만 맞음...

prices = [1, 2, 3, 2, 3]


def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1
        answer.append(count)
    return answer
