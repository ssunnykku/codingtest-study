# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 9시까지
# 다시 풀어봐야 할 듯
from collections import deque

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
answer = 0
visited = []

queue = []

for i in range(n):
    if i not in visited:
        queue.append(i)
        answer += 1
        for j in range(n):
            if computers[i][j] not in visited and 1:
                visited.append(j)
                print(visited)

    # for j in computers[i]:
    #     print(j)
