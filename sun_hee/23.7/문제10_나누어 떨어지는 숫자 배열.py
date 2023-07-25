# https://school.programmers.co.kr/learn/courses/30/lessons/12910

arr=[2, 36, 1, 3]
divisor=1

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor ==0:
            answer.append(i)
            answer.sort()
    if answer == []:
        return [-1]
    return answer

print(solution(arr,divisor))