def solution(a, b):
    # 최대공약수 구하기
    x = a
    y = a
    while x != 0 and y != 0:
        if x > y:
            x = x - y
        else:
            y = y - x
    z = b/(x + y)


print(solution(11, 22))
