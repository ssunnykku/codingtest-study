# https://school.programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = f'김서방은 {i}에 있다'
    return answer