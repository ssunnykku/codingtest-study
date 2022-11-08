def solution(a, b):
    smallNum = 0
    BNum = b
    if a >= b:
        smallNum = b
    else:
        smallNum = a
    maxNum = 1
    BNumArray = []
    answerArray = []
    answer = 0
#     최대공약수 구하기
    for i in range(1, smallNum+1):
        if (a % i == 0) and (b % i == 0):
            if (maxNum < i):
                maxNum = i
  # 분모를 최대 공약수로 나누고 약수 구하기
    BNum = int(b/maxNum)
    for i in range(2, BNum+1):
        if (BNum % i == 0):
            BNumArray.append(i)
    # 약수 중 2나5로 나눠지면 1을 아니면 2을 배열에 넣어주기
    for i in BNumArray:
        if (i % 2 == 0):
            answerArray.append(1)
        elif (i % 5 == 0):
            answerArray.append(1)
        else:
            answerArray.append(2)
    # answerArray 중에서 2가 포함되어있다면 answer에 2를 넣어주고 break 아니면 answer에 1을 넣어주고 반환
    print('answerArray :', answerArray)
    for i in answerArray:
        if i == 2:
            answer = 2
            break
        else:
            answer = 1
    return answer

    print(solution(7, 210))
