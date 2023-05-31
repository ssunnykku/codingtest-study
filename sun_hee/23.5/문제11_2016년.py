# https://school.programmers.co.kr/learn/courses/30/lessons/12901?language=python3
a = 5
b = 25


def solution(a, b):
    arr = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    x = sum(date[0:a]) - (date[a - 1] - b)
    answer = arr[x % 7 - 1]
    return answer


print(solution(a, b))
