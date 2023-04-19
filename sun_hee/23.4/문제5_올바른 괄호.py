# https://school.programmers.co.kr/learn/courses/30/lessons/12909

s = ')'

# 주어진 s를 순회
def solution(s):
    stack = []

    for i in s:
        #     왼쪽 괄호면 stack에 넣어줌
        if i == '(':
            stack.append(i)
        # 스택이 비었는데 ")" 만나면?
        elif i == ")" and stack == []:
            return False
        elif i == ")":
            stack.pop()
    if stack == []:
        return True
    else:
        return False

print(solution(s))