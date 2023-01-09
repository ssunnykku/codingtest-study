# 짝수라면 2로 나누기
# 홀수라면 3을 곱하고 1을 더하기
# 1이 될 때까지 반복하기
# 1이면 0을, 500번 이상 반복 후에는 -1

n = 6
# n = 16
cnt = 0
if n == 1:
    print(0)
while n != 1:
    if n % 2 == 0:
        n = n // 2
        cnt += 1
    elif n % 2 != 0:
        n = n * 3 + 1
        cnt += 1
    if n == 1:
        print(cnt)
        break
    if cnt >= 500:
        print(-1)
        break

# print(cnt)
# print(n)
