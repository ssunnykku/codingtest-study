# n은 가로, m은 세로
n, m = map(int, input().split())
# (a,b) : 현재위치, d : 방향
a, b, d = map(int, input().split())

first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))
fourth = list(map(int, input().split()))

# 북, 동, 남, 서
# 0, 1, 2, 3
# -4, -3, -2, -1
direction = [0, -1, -2, -3]
now = [a, b]
# 0: 육지, 1: 바다
# 만약 d = 0(북쪽) 이라면 B, now[1] -1 탐색
# 만약 d = -1(동쪽) 이라면 A, now[0] +1 탐색
# 만약 d = -2(남쪽) 이라면 B, now[1] +1 탐색
# 만약 d = -3(서쪽) 이라면 A, now[0] -1 탐색

# 만약 바다이면 왼쪽을 탐색 
if d == 0:
    now[1] -= 1
    print(now)
if d == -1:
    now[0] += 1
    print(now)
if d == -2:
    now[1] += 1
    print(now)
if d == -3:
    now[0] -= 1
    print(now)
