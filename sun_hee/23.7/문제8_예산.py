# https://school.programmers.co.kr/learn/courses/30/lessons/12982

d = [1,3,2,5,4] 
budget = 9

# d : 부서별 신청 예산
# budget : 최대 예산
# Q : 최대 몇 개의 부서에 제공 가능한지?

def solution(d, budget):
    d.sort()
    sum_budget = 0
    answer = 0

    for i in d:
        sum_budget += i
        if sum_budget > budget:
            break
        answer += 1
   
    return answer

print(solution(d,budget))