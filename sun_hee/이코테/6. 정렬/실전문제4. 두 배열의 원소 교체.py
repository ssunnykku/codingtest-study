# 두 개의 배열 a와 b, n개의 원소로 되어있음, 배열 모두는 자연수
# 최대 K번의 바꿔치기를 한다 (a 원소와 b 원소 바꾸기)
# 목표 : a의 모든 원소의 값이 최대가 되도록 하는 것
# 배열 a의 모든 원소의 합의 최댓값을 출력해라

n, k = map(int, input().split())


a, b = list(map(int, input().split())), list(map(int, input().split()))

# n, k = 5, 3

# a = [1, 2, 5, 4, 3]
# b = [5, 5, 6, 6, 5]

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
