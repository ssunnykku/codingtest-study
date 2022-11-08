def solution(n, lost, reserve):
    # n만큼 1로 clothArray채우기
    clothArray = [1 for i in range(n)]
    answer = 0

    # lost에 속하면 clothArray -1해주기
    for i in lost:
        for j in range(n):
            if (i-1) == j:
                clothArray[j] -= 1
    # reserve에 속하면 clothArray +1해주기
    for i in reserve:
        for j in range(n):
            if (i-1) == j:
                clothArray[j] += 1
    # 양 옆 사람한테 체육복 빌려쥐기
    for i in range(n):
        # n-1일때랑 i=0일 때는 한쪽에서만 주고받을 수 있으므로 예외처리
        if (i == (n-1)) or (i == 1):
            if clothArray[i] == 2 and clothArray[i-1] == 0:
                clothArray[i] -= 1
                clothArray[i-1] += 1
            elif clothArray[i] == 0 and clothArray[i-1] == 2:
                clothArray[i] += 1
                clothArray[i-1] -= 1
        # 그 외
        else:
            if clothArray[i] == 0 and clothArray[i-1] == 2:
                clothArray[i] += 1
                clothArray[i-1] -= 1
            elif clothArray[i] == 0 and clothArray[i+1] == 2:
                clothArray[i] += 1
                clothArray[i+1] -= 1

    for i in clothArray:
        if i != 0:
            answer += 1
    print(clothArray)
    return answer
