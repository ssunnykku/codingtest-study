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

    list = []
    for i in range(1, int(z+1)):
        list.append(z/i)
        if len(list) >= 3:
            return 2
        if len(list) == 2:
            for i in range(list):
                if i == 2 and i == 5:
                    return 1
                else:
                    return 2
        if len(list) == 1:
            if i == 2 or 5:
                return 1
            else:
                return 2


print(solution(11, 22))
