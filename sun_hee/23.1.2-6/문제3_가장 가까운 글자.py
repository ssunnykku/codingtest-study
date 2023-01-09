
# 앞에 같은 글자 없으면 -1
# 같은 글자 있으면 index 빼준 값 출력 (가까운 값 출력)
# 자신의 앞만 탐색

# a.insert(index,number) : index 순서에 number 넣어라. 원래 그 자리에 있던 값은 뒤로 밀린다.

s = "banana"
a = []
for i in range(0, len(s)):
    if s[i] not in s[:i]:
        a.append(-1)
    elif s[i] in s[:i]:
        #  s[:i] : 비교할 값
        for j in range(len(s[:i])):
            # print(s[i], s[:i][j])
            if s[i] == s[:i][j]:
                # print(i, j)
                if len(a) == i:
                    a.append(i-j)
                else:
                    a[i] = i-j

# print(a)

# 하은이의 풀이

s = "banana"

# filter 내장함수
# filter(조건 함수, 순회 가능한 데이터)


def solution(s):
    answer = []
    temp = []
    for i in s:
        if i not in temp:
            temp.append(i)
            answer.append(-1)
        elif i in temp:
            temp.append(i)
            rest_list = list(filter(lambda x: temp[x] == i, range(len(temp))))
            answer.append(rest_list[-1] - rest_list[-2])

    return answer


# print(solution(s))
