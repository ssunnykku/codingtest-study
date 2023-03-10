# https://www.acmicpc.net/problem/18406

n = list(map(int, input()))

front = sum(n[:int(len(n)/2)])
back = sum(n[int(len(n)/2):])

if front == back:
    print('LUCKY')
else:
    print('READY')
