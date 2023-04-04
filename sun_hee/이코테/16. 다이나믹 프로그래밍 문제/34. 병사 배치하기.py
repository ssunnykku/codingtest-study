# https://www.acmicpc.net/problem/18353

# 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치
# 앞쪽 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 한다.
# 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병서의 수를 출력
# 나의 답안(틀림)
# n = int(input())

# array = list(map(int,input().split()))

# cnt = 0

# for i in range(n-1):
#     if array[i]<array[i+1]:
        
#         cnt += 1
# print(cnt)

# 교재 답안
# n = int(input())

# array = list(map, input().split())
n = 7
array = [15, 11, 4, 8, 5, 2, 4]

array.reverse()

dp = [1] * n
for i in range(1,n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

# 열외시켜야 하는 병사의 최소 수
print(n-max(dp))