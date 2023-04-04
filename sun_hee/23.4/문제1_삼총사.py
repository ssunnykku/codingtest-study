# https://school.programmers.co.kr/learn/courses/30/lessons/131705
# 세명의 번호를 더해서 0이면 삼총사
number = [-2, 3, 0, 2, -5]

count = 0

for i in range(len(number)):
    for j in range(i+1, len(number)):
        for k in range(j+1, len(number)):
            result = number[i]+number[j]+number[k]
            if result == 0:
                count += 1
print(count)