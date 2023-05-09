# https://school.programmers.co.kr/learn/courses/30/lessons/42586
#  11시 20분까지
from collections import deque
import math

progresses = [30]
speeds = [30]
# 배포까지 필요한 날짜 계산하여 리스트에 담기
# 100-93 = 7
# 7 / 1

# 한번에 몇개 배포 되는지 세기


def solution(progresses, speeds):
    p = deque(progresses)
    s = deque(speeds)
    deployments = []

    while p:
        progress = p.popleft()
        speed = s.popleft()
        count = math.ceil((100 - progress) / speed)
        deployments.append(count)
        #  d :  개발 횟수 구하기

        d = deque(deployments)
        answer = []
        cnt = 1
        compare = d.popleft()
        if len(d) == 0:
            answer.append(cnt)
    for i in deployments[1:]:
        if compare >= i:
            cnt += 1
            if len(list(d)) == 1:
                answer.append(cnt)
            d.popleft()
        elif compare < i:
            answer.append(cnt)
            cnt = 1
            if len(list(d)) == 1:
                answer.append(cnt)
            compare = d.popleft()
    return answer


print(solution(progresses, speeds))

# deployments를 가지고 개발 횟수 어떻게 구하지?
# list = [7, 2, 9]
# l = deque([7, 2, 9])

# # 7보다 큰 수가 나올 때까지 leftpop 하기

# first = l.popleft()
# answer = []
# cnt = 1
# for i in list[1:]:
#     if first >= i:
#         cnt += 1
#         l.popleft()
#     else:
#         answer.append(cnt)
#         cnt = 0
#         first = l.popleft()
#         answer.append(1)

# print(answer)
