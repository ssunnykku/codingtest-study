# a = str(input())
# b = str(input())

a = 'sunday'
b = 'saturday'

if a == b:
    print(0)

pd = [0] * len(b)
cnt = 0

for i in range(len(a)):
    if b[i] != a[i]:
        cnt += 1

print(cnt)
