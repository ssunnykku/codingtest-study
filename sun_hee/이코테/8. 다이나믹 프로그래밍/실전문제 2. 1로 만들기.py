# X가 5로 나누어 떨어지면 5로 나눈다
# X가 3으로 나누어 떨어지면 3으로 나눈다
# X가 2로 나누어 떨어지면 2로 나눈다
# X에서 1을 뺸다

# 1을 만들기

# x = int(input())
x = 26
d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if x % 5 == 0:
        d[i] = min(d[i], d[i // 5]+1)
    if x % 3 == 0:
        d[i] = min(d[i], d[i // 3]+1)
    if x % 2 == 0:
        d[i] = min(d[i], d[i // 2]+1)

print(d[x])
