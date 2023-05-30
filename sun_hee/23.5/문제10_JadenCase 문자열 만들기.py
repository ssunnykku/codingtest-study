# https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=python3

s = "3people unFollowed  me"


# 알파벳 숫자 공백문자
#  숫자는 첫 문자로만
def solution(s):
    s = s.split(" ")
    answer = ""
    for i in range(len(s)):
        answer += s[i][0].upper() + s[i][1:].lower() + " "

    return answer[:-1]
