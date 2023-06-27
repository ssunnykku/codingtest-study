# https://school.programmers.co.kr/learn/courses/30/lessons/12924

n = 15


def solution(n):
    cnt = 0
    array = list(range(1, n + 1))
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            s = sum(array[i:j])
            if s == n:
                cnt += 1
            elif s > n:
                break
    return cnt


print(solution(n))
