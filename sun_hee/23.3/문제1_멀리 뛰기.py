# https://school.programmers.co.kr/learn/courses/30/lessons/12914?language=python3

# 1,2 리스트 만들기
# 더해서 n이 되는 조합 찾기
# 첫 칸이 1일 경우, 2일 경우의 조합 찾기

# 틀림, 흰트 : 다이나믹 프로그래밍
n = 4
count = 0
array = [1,2]
for i in range(n-1):
    sum = 0
    if sum <= n-1:
        for j in array:
            count += 1
            sum += i

for i in range(n-2):
    sum = 0
    if sum <= n-2:
        count += 1
        sum += i

print(count%1234567)