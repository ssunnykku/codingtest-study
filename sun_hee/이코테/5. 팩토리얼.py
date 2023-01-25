# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result


# 재귀적으로 구현한 n!
# 0!과 1!의 값은 1로 같으므로 n이 1 이하가 되었을 때 함수를 종료
def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n * (n-1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)


print("반복적으로 구현:", factorial_iterative(5))
print("재귀적으로 구현:", factorial_recursive(5))
