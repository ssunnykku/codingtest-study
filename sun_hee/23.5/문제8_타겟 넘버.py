# https://school.programmers.co.kr/learn/courses/30/lessons/43165
from collections import deque

numbers = [1, 1, 1, 1, 1]
target = 3
gragph = [[], [+1, -1], [+1, -1], [+1, -1], [+1, -1]]
visited = [False] * len(gragph)

queue = deque([1])
dp = []
# visited[1] = True

while queue:
    v = queue.popleft()
    for i in gragph[v]:
        if visited[i] == False:
            queue.append(i)
            visited[i] = True
    print(queue)

print(visited)
# print(queue)
