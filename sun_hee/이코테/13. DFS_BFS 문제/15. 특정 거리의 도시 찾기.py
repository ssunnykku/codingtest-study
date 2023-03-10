# n = 4  # 도시의 개수
# m = 4  # 도로의 개수
# k = 2  # 거리 정보
# x = 1  # 출발 도시의 번호

# # 1 2
# # 1 3
# # 2 3
# # 2 4

# n, m, k, x = map(int, input().split())
# graph = [[]]
# for i in range(m):
#     graph.append(list(map(int, input().split())))

# visited = [False] * m


# def dfs(graph, v, visited):
#     visited[v] = True
#     if v == k:
#         print(v)

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)


# dfs(graph, x, visited)

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[]]
for i in range(m):
    a, b = map(int, input().split())
    graph.append([a, b])

visited = [False] * (m+1)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    result = False
    while queue:
        v = queue.popleft()
        if v == k:
            print(v)
            result = True
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    if result == False:
        print(-1)


bfs(graph, x, visited)
