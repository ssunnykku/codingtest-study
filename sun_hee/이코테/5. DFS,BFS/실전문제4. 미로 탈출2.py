from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v+1, end=" ")
        # 해당 원소와 연결된, 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True


n, m = map(int, input().split())
# 괴물, 0, 없으면 1

graph = [list(map(int, input().split())) for i in range(n)]

visited = [False] * n
start = 1-1


bfs(graph, start, visited)
