n = int(input())
r = []
for i in range(n): 
    r.append(list(map(int,input().split())))

for i in range(1,len(r)):
    for j in range(len(r[i])):
        # 왼쪽에서 오는 경우
        if j == 0:
            left_up = 0
        else:
            left_up = r[i-1][j-1]

        # 오른쪽에서 오는 경우
        if j == i:
            right_up = 0
        else:
            right_up = r[i-1][j]
        r[i][j] += max(left_up, right_up)
print(max(r[-1]))

# 교재 정답
# n = int(input())
# dp = [] # DP 테이블 초기화

# for _ in range(n):
#     dp.append(list(map(int, input().split())))

# # 다이나믹 프로그래밍으로 두 번째 줄부터 내려가면서 확인
# for i in range(1,n):
#     for j in range(i+1):
#         # 왼쪽 위부터 내려오는 경우
#         if j == 0:
#             up_left = 0
#         else:
#             up_left = dp[i-1][j-1]
#         # 바로 위에서 내려오는 경우
#         if j == i:
#             up = 0
#         else:
#             up = dp[i-1][j]
#         # 최대 합을 저장
#         dp[i][j] = dp[i][j] + max(up_left, up)

# print(max(dp[n-1]))
              