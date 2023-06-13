# https://school.programmers.co.kr/learn/courses/30/lessons/12985

# N명이 참가
n = 8
a = 4
b = 7

import math


def solution(n, a, b):
    answer = 1

    while math.ceil(a / 2) != math.ceil(b / 2):
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1

    return answer


print(solution(n, a, b))
