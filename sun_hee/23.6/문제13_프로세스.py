# https://school.programmers.co.kr/learn/courses/30/lessons/42587
priorities = [1, 1, 9, 1, 1, 1]

location = 0

def solution(priorities, location):
    # 요소들을 "q"로 채운 array
    array = ["q" for _ in priorities]
    # 해당 위치는 "this"로 채워준다
    array[location] = "this"

    answer = 0

    while len(priorities) > 0:
        # 우선순위를 확인, 
        if max(priorities) > priorities[0]:
            first = priorities.pop(0)
            element = array.pop(0)
            # 우선순위가 제일 높지 않으므로 맨 뒤로 다시 넣어줌
            priorities.append(first)
            array.append(element)

        # 우선순위가 제일 높은 경우
        elif max(priorities) <= priorities[0]:
            priorities.pop(0)
            element = array.pop(0)
            # 하나를 처리했으므로 answer에 1을 카운트
            answer = answer+1
            # 만약 현재 처리한 요소가 "this"라면 answer을 반환하고 함수를 종료한다.
            if element == "this":
                return answer

print(solution(priorities, location))