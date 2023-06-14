# https://school.programmers.co.kr/learn/courses/30/lessons/12911

# 9시까지?!!
# 2진법 구해보기
n = 78
# array = []
# array.append(n % 2)
# while n > 1:
#     n = n // 2
#     array.append(n % 2)
# array2 = [str(i) for i in array[::-1]]

# result = "".join(array2)
# print(result)


def solution(n):
    x = n
    # 처음 n의 2진수를 구해서 리스트에 담기
    array = []
    array.append(x % 2)
    while x > 1:
        x = x // 2
        # 나머지를 array에 담기
        array.append(x % 2)
        # 1의 갯수를 구하기
    result = array.count(1)

    while True:
        cal = []
        # 1 더해주며 반복
        n = n + 1
        a = n
        cal.append(n % 2)
        while a > 1:
            a = a // 2
            cal.append(a % 2)
            # 1의 갯수가 같은 값이 나오면 함수를 종료함
        if cal.count(1) == result:
            break

    return n


print(solution(n))
