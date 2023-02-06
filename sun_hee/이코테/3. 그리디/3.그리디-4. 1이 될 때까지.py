# 7시 54분 ~ 8시 24분 // 15분

# N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 수행, 두번 째는 N이 K로 나누어 떨어질 때만 선택
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다

# 풀이
# N % K가 0이면 N // K값을 저장
# cnt에 1을 더해주기
# N % K가 0이 아니라면 1을 빼기
# cnt에 1을 더해주기
# N이 1이 될 때까지 반복

# 경우의 수 생각하기. 9 1이 입력된다면 ? 무한루프가 돌 수 있다.
# k가 1일 경우..
# K가 2 이상이기만 하면 K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N의 값을 줄일 수 있으며 N이 결국 1에 도달한다는 것을 알 수 있다.

n, k = map(int, input().split())

cnt = 0

while True:
    if n <= 1:
        break
    if k == 1:
        cnt = n-1
        break
    elif n % k == 0:
        n = n // k
        cnt += 1
    else:
        n -= 1
        cnt += 1
    if n <= 1:
        break

print(cnt)


# 교재풀이, 간단버전
n, k = map(int, input().split)
result = 0
# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K 이상이라면 K로 계속 나누기
    while n % k != 0:
        n -= 1
        result += 1
    # k로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)

# 교재 풀이2 어렵군하..
n, k = map(int, input().split)
result = 0

while True:
    target = (n // k) * k
    result += (n-target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
