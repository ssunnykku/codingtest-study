def solution(A, B):
    listA = list(A)
    listB = list(B)
    meetB = []
    answer = -1

    # listA[0]하고 listB가 일치하는 인덱스 번호찾기
    for j in range(len(listB)):
        if listA[0] == listB[j]:
            meetB.append(j)
    # listA하고 listB하고 얼마나 밀어야 일치하는지 찾기

    for i in meetB:
        for j in range(len(listA)):
            if listA[0] == listB[i] and listA[-j] == listB[i-j]:
                answer = i
            else:
                answer = -1
        if answer != -1:
            break

    return answer
