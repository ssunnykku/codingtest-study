# https://school.programmers.co.kr/learn/courses/30/lessons/12980

n = 6

def solution(n):
    ans = 0
    
    while True:
        if n % 2 == 0:
            n = n/2
        else:
            n = (n-1)/2
            ans += 1    
        if n ==0:
            break
    return ans

print(solution(n))