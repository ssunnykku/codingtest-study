# n x m 크기의 금광 
# 채굴자가 얻을 수 있는 금의 최대 크기를 출력
# 다시다시

for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int,input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
                