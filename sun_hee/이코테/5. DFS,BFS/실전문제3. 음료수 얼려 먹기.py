# DFS를 이용하는 문제

# input
# 세로 길이 N , 가로 길이 M
# 얼음 틀의 형태
#  구멍 0, 아니면 1

# 1. 상, 하, 좌, 우를 살펴보고 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
# 2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면 연결된 모든 지점을 방문할 수 있음
# 3. 1~2번 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


#  모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
print(result)
