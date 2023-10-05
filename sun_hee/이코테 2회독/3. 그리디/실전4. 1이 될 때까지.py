# 무조건 N을 K로 나누기
# 만약 나머지가 0이 아니라면 빼기

n, k = map(int, input().split())

cnt = 0

while True:
    if n == 1:
        break
    if n % k != 0:
        n = n-1
        cnt += 1
    elif n % k == 0:
        n = n // k
        cnt += 1
    

print(cnt)

