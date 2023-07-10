# https://school.programmers.co.kr/learn/courses/30/lessons/159994

cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"] 

def solution(cards1, cards2, goal):
    answer = ''
    for i in cards1:
        if i in goal:
            index = goal.index(i)
            del goal[index]
    for i in cards2:
        if i in goal:
            index = goal.index(i)
            del goal[index]
    if goal == []:
        return "yes"
    else:
        return "no"

print(solution(cards1, cards2, goal))