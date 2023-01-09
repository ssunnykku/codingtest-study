# 9시 35분 ~10시 5분

# 인덱스 기준으로 문제 다시 정리
# array[i-1:j]
# 정렬하기(오름차순)
# k-1번째 있는 수를 구하기

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer = []
for command in commands:
    i = command[0]
    j = command[1]
    k = command[2]
    answer.append(sorted(array[i-1:j])[k-1])
