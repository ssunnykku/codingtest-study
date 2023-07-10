# https://school.programmers.co.kr/learn/courses/30/lessons/12918

s = "123ABC"
# s = "12345" 
# false

def solution(s):
    alpabet =  "abcdefghijklmnopqrstuwxyz"
    
    if len(s) == 4 or len(s) == 6:
            for i in s:
                 if i.lower() in alpabet:
                      return False
    elif len(s)!= 4 or len(s)!= 6:
        return False
    
    return True


print(solution(s))