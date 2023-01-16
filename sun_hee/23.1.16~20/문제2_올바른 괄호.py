# 10분만 풀어보자
# ()
# ()()

s = "()()"
# s = "(())()"

# s = ")()(" # f
# s = "(()(" # f

# ( 로 끝나면 f
# )로 시작하면 f
# 갯수가 홀수면 f
# 짝이안맞으면 f
left = 0
right = 0

if s[0] == ")":
    print("false")
if s[-1] == "(":
    print("false")
if len(s) % 2 != 0:
    print("false")
for a in s:
    if a == "(":
        left += 1
    else:
        right += 1
    if left != right:
        print("false")
    else:
        print("true")
