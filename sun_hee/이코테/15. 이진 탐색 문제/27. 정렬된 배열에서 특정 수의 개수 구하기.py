# n개의 원소 수열 오름차순 정렬, x가 등장하는 횟수를 계산
# n, x = map(int, input().split())

# list=list(map(int, input().split()))
ß
n = 7
x = 2
list = [1,1,2,2,2,2,3]

if list.count(x) == 0:
    print(-1)
else:
    print(list.count(x))

