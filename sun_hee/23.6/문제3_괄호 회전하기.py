# https://school.programmers.co.kr/learn/courses/30/lessons/76502
s = "}]()[{"


def solution(s):
    array = [s]
    answer = 0
    for i in range(len(s) - 2):
        s = s[1:] + s[0]
        array.append(s)
    for i in array:
        stack = []
        for j in i:
            if j == "[" or j == "(" or j == "{":
                stack.append(j)

            elif j == "]" or j == ")" or j == "}":
                if stack == []:
                    answer -= 1
                    break
                if stack[-1] == "(" and j == ")":
                    stack.pop()
                elif stack[-1] == "{" and j == "}":
                    stack.pop()
                elif stack[-1] == "[" and j == "]":
                    stack.pop()
        if stack == []:
            answer += 1

    return answer


print(solution(s))
