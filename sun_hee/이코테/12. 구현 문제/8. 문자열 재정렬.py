s = list(map(str, input()))
s.sort()
a = 0
result = []
# result = [i if i.isalpha() == True else "No" for i in s]
for i in s:
    if i.isalpha() == True:
        result.append(i)
    else:
        a += int(i)
result.append(a)
print(''.join(result))
