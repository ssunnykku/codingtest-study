import time
# 풀이시간 15분 : 3시 37분까지!!
# 시간제한 1초, 메모리 제한 128MB

# L : 왼1칸, R: 오른1칸, : y축, 오른쪽 값
# U:위1칸, D:아래1칸
# N : 공간의 크기

# ------------------------------------------------------------------
# 나의 풀이 1. 실패
# time : 5.320566892623901

# n = 5
# route = ["R", "R", "R", "U", "D", "D"]

# start = time.time()
# n = int(input())
# 리스트로 입력받기
# 문자면 굳이 이렇게 하지말고 input().split() 이렇게 받기!!
# route = list(map(str, input().split()))


def find_index(n, route):
    result = [1, 1]
    for order in route:
        # "R이면 result[1]에 1더해주기.""
        if order == "R":
            # 단 result[1]이 n보다 작을 때만
            if result[1] < n:
                result[1] += 1
        elif order == "L":
            if result[1] > 1:
                result[1] -= 1
        elif order == "U":
            if result[0] > 1:
                result[0] -= 1
        elif order == "D":
            if result[0] < n:
                result[0] += 1
    return ' '.join(list(map(str, result)))


# print(find_index(n, route))

# print("time :", time.time() - start)

# 교재 답안
# 시뮬레이션 유형: 명령에 따라 개체를 차례대로 이동시킴
# 이 문제를 요구사항대로 구현하면 연산 횟수는 이동 횟수에 비례하게 된다. 예를 들어 이동 횟수가 N번인 경우 시간 복잡도는 O(N)이다.

start = time.time()
# N을 입력받기
n = int(input())
x, y = 1, 1
# 헐..
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

# 이동 계획을 하나씩 획인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경로 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
print("time :", time.time() - start)
# time : 5.338950872421265
