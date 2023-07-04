# https://school.programmers.co.kr/learn/courses/30/lessons/42577#qna

# https://school.programmers.co.kr/questions/39655

#  실패.. 시간 초과... ㅠㅠ
phone_book = ["123","456","789"]

def solution(phone_book):
    for i in phone_book:
        for j in range(1,len(i)):
            first = i[:j]
            if first in phone_book:
                return False
    return True



print(solution(phone_book))