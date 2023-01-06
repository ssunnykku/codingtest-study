# 문자열 s 한 개 이상의 단어
# 공백문자로 구분
# 짝수번째 : 대문자, 홀수번째 : 소문자로

s = "try hello world"

s_list = s.split(" ")
result = ""

for j in range(len(s_list)):
    for i in range(len(s_list[j])):
        if i % 2 == 0:
            result += str(s_list[j][i]).upper()

        elif i % 2 != 0:
            result += str(s_list[j][i]).lower()

    if j != len(s_list)-1:
        result += " "
print(result)
