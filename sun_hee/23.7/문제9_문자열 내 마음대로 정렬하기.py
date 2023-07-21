# https://school.programmers.co.kr/learn/courses/30/lessons/12915

strings = ["abce", "abcd", "cdx"]
n= 2
# n번째 글자를 기준으로 오름차순 정렬

def solution(strings, n):
    strings = sorted(strings)
    answer = sorted(strings, key=lambda x:x[n])
    return answer

print(solution(strings,n))