# 6시 30분까지!!
# https://school.programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque

people = [50, 50, 79, 80]
limit = 100
# limit : 40 이상 240 이하
# 1. limit 보다 크기가 작아야 함
# 2. 2명만 탈 수 있음
# 정렬해보기 [50, 50, 79, 80]
# 40~60 키로인 사람들만 후보에 듦
# 후보군의 조건을 만들기. 40키로~limit-40
# people = [40, 50, 150, 160]
# limit = 200

# 테스트 케이스만 맞고 틀리다고 함


def solution(people, limit):
    # max: 2인 탑승 가능 최댓값
    max = limit - 40
    c = []
    cnt = 0
    for one in people:
        if one <= max:
            c.append(one)
            # 후보군에 들지 않은 사람들은 혼자 타기
        else:
            cnt += 1
    c.sort(reverse=False)

    def find(c):
        cnt2 = 0
        s = deque(c)
        for a in list(s)[:-1]:
            if s[-1] + a <= 250:
                s.pop()
                s.popleft()
                print(s)
                cnt2 += 1
                if s == deque([]):
                    break

        if s != deque([]):
            cnt2 += len(s)
        return cnt2

    cnt += find(c)

    return cnt


print(solution(people, limit))

# 2명씩 묶어보자!

# list = [40, 50, 150, 160]


# def find(list):
#     list2 = sorted(list, reverse=False)

#     def find2(list2):
#         s = deque(list2)
#         for i, a in enumerate(list2):
#             if list2[-1] + a <= 250:
#                 print(s.pop())
#                 s.popleft()

#         if s == deque([]):
#             print("그래?")

#     find2(list2)


# find(list)
