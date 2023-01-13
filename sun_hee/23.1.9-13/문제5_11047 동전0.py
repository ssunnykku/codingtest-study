# 8분 ~ 30분

# 동전 N종류
# 그 가치의 합을 K로 만들기
# 필요한 동전 갯수의 최솟값 구하기

# N과 K가 주어진다
# N개의 줄에 동전의 가치 Aj가 오름차순으로 주어진다
# coins = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
# K = 4200

# 풀이
# 반복문을 돌리다가
# K 보다 작은 동전의 수를 모두 찾기, 오름차순으로 정렬
# 1000, 500, 100, 50, 10, 5, 1
# coin이 하나의 동전이라고 할 때
# 4200 // coin 를 동전의 수에 더하기
# 4200 % coin = coin
# 0이 될 때 까지

N, K = input().split()
coins = [int(input()) for i in range(int(N))]

x = sorted(coins, reverse=True)
cnt = 0
for coin in x:
    if coin <= int(K):
        cnt += int(K) // coin
        K = int(K) % coin
print(cnt)

# 맞았음
# 메모리 : 30616KB
# 시간 : 40ms

# 다른 사람 코드
# n,k,a=*map(int, input().split()),0
# for i in [int(input()) for _ in '.'*n][::-1]:
#     a+=k//i
#     k%=i
# print(a)
