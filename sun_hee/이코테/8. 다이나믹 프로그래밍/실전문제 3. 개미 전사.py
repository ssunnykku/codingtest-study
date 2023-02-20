# 한 칸 이상 떨어진 식량 창고를 약탈해야 한다.
#  식량창고 N개에 대한 정보가 주어졌을 때 엇을 수 있는 식량의 최댓값 구하기

n = int(input())

k = list(map(int, input().split()))

d = [0] * n

# for i in range(n):
#     if i % 2 == 0:
#         d[0] += k[i]
#     if i % 2 != 0:
#         d[1] += k[i]

# print(max(d))

d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n-1])
