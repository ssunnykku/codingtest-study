# https://school.programmers.co.kr/learn/courses/30/lessons/68935

n = 45

def solution(n):
    answer = 0
# 10 -> 3진법으로
    three = ''
    while n >= 1:
        three += str(n % 3)
        n = n // 3
# 3 -> 10진법으로
    three = int(three)
    three = str(three)[::-1]

    for i in range(len(three)):
        mul = pow(3,i) *int(three[i])
        answer += mul
    
    return answer

print(solution(n))