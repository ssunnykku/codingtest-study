# 내 코드는 안돌아간다..
ugly = [2,3,5]

n = 10

dp = [0]*n
m = 1
for i in range(n):
    list = []
    u = 2
    if m == 15:
        break

    while True:
        if m == 1:    
            dp[m] += 1
            break
        if m % u == 0:
            list.append(u)
            m = m // u
            print(m)
        else:    
            u += 1
            continue
    m += 1
    print(m, list)
    # for i in list:
    #     dp[m] += 1
    #     if i not in ugly:
    #         continue

    # if len(dp) == n+1:
    #     break
    
# print(dp)

# 교재 답안
n = int(input())

# 2의 배수, 3의 배수, 5의 배수 변수에 대하여 각각 '가장 작은 못생긴 수'부터 오름차순으로 하나씩 확인하면서 각 배수를 곱한 값도 '못생긴 수'가 되도록 한다.
ugly = [0] * n # 못생긴 수를 담기 위한 테이블(1차원 DP 테이블)
ugly[0] = 1 # 첫 번째 못생긴 수는 1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

for i in range(1,n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    ugly[i] = min(next2, next3, next5)
    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5
    
print(ugly[n - 1])
        
    