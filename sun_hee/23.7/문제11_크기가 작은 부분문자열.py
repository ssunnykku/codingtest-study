# https://school.programmers.co.kr/learn/courses/30/lessons/147355

t = "3141592"
p = "271"

def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        num = t[i:i+len(p)]
        if int(num) <= int(p):
            answer += 1

    return answer

print(solution(t,p))