# N = 5
# M = 8
# K = 3

# 5 8 3
# 2 4 5 4 6


def num(N, M, K):
    result = None
    return result

# 입력된 배열을 내림차순으로 나열, 큰 수를 찾아서 K번 리스트에 넣기
# 두번째 큰 수 1번 리스트에 넣기
# 전체 길이가 8보다 크면 멈추기
# 8개까지 더해서 출력


# # 과정
# N = 5
# M = 8
# K = 3
# list = sorted([2, 4, 5, 4, 6], reverse=True)

# big = []

# while True:
#     for i in range(K):
#         big.append(list[0])
#     big.append(list[1])
#     if len(big) > M:
#         break

# print(sum(big[:M]))

# 최종

# condition = list(map(int, input().split()))
# list = sorted(list(map(int, input().split())), reverse=True)

# N = condition[0]
# M = condition[1]
# K = condition[2]

# big = []

# while True:
#     for i in range(K):
#         big.append(list[0])
#     big.append(list[1])
#     if len(big) > M:
#         break

# print(sum(big[:M]))

# # 교재풀이 1
# # N, M, K를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())

# # N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))

# data.sort()  # 정렬
# first = data[n - 1]  # 가장 큰 수
# second = data[n - 2]  # 두 번째로 큰 수

# result = 0

# while True:
#     for i in range(k):  # 가장 큰 수를 K번 더하기
#         if m == 0:
#             break    # m이 0이라면 반복문 탈출
#         result += first
#         m -= 1  # 더할 때마다 1씩 빼기
#     if m == 0:  # m이 0이라면 반복문 탈출
#         break
#     result += second  # 두 번째로 큰 수를 한 번 더하기
#     m - + 1  # 더할 때마다 1씩 빼기

# print(result)

# 교재 풀이 2 (다시 보기)
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수 정렬
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m-count) * second  # 두 번째로 큰 수 더하기

print(result)
