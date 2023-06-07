# https://school.programmers.co.kr/learn/courses/30/lessons/12945
# 0,1,1,2,3,5
# 2 이상의 n이 입력되었을 때 n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴

n = 5


def solution(n):
    d = [0, 1]
    if n == 2:
        return d[-1] % 1234567
    for i in range(2, n + 1):
        d.append(d[i - 1] + d[i - 2])

    answer = d[-1] % 1234567
    return answer


print(solution(n))
