# https://school.programmers.co.kr/learn/courses/30/lessons/68644

numbers = [2, 1, 3, 4, 1]


def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(1, len(numbers) - i):
            answer.append(numbers[i] + numbers[-j])

    return sorted(list(set(answer)))


print(solution(numbers))
