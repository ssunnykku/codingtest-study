# https://school.programmers.co.kr/learn/courses/30/lessons/86491

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]


def solution(sizes):
    array = []
    for i in sizes:
        for j in i:
            array.append(j)
    x = max(array)
    array2 = []
    for i in sizes:
        array2.append(min(i))
    y = max(array2)
    return x * y


# 왼쪽 기준으로 정렬

print(solution(sizes))
