# https://school.programmers.co.kr/learn/courses/30/lessons/43105  (동적계획법)

# 11시까지


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def solution(triangle):
    d = []
    d.append(triangle[0])
    for j, a in enumerate(triangle[1:]):
        line = [0] * (j + 2)
        for i, b in enumerate(a):
            if i == 0:
                line[i] += d[j][0] + triangle[j + 1][i]
            elif i == len(a) - 1:
                line[i] += d[j][-1] + triangle[j + 1][i]
            else:
                line[i] = max(d[j][i], d[j][i - 1]) + triangle[j + 1][i]
        d.append(line)
    answer = max(d[-1])
    return answer
