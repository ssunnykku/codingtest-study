s = input()

# 0,1일 경우 더하기

result = 0

for i in s:
    if int(i) <= 1:
        result += int(i)

    elif int(i) > 1:
        if result == 0:
            result += int(i)
        else:
            result *= int(i)

print(result)