# https://school.programmers.co.kr/learn/courses/30/lessons/42578

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

# 종류별 하나만 착용 가능 

def solution(clothes):
    answer = 0
    pair = {}
    combination = []
    for cloth in clothes:
        pair[cloth[0]] = cloth[1]
    for i in pair:
        print(i)

    return answer

print(solution(clothes))  