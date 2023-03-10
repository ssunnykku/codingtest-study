# 균형잡힌 : ( ) 갯수가 맞을 때
# 올바른 : ( ) 짝이 맞을 때

# 1. 빈 문자열 => 빈 문자열을 반환
list = "()))(())"
stack = []
a = []
stack.append(list[0])
result = True

for i in range(len(list[1:])):
    print(i)
    if list[i+1] == "(":
        if list[i] == ")":
            a.append(stack.pop())
            stack.append(list[i+1])
            stack.append(list[i])
        else:
            stack.append(list[i+1])
    elif list[i+1] == ")" and stack == []:
        stack.append(list[i+1])
    elif list[i+1] == ")" and stack[-1] == "(":
        a.append(stack.pop())

print(a)
print(stack)
if stack == []:
    print(list)
