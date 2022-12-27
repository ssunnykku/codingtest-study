#  빈병 a개를 가져다주면 콜라 b 병을 줌, n 병을 주었을 때 몇 병을 받을 수 있나?

#  상빈이 문제 부터 풀어보기. 빈병 2개 당 콜라 1개,

# n = 20

# result = 0

# while n >= 2:
#     cock = n//2
#     result += cock
#     n -= cock
#     if n < 2:
#         break

# 일반화하기

a = 3
b = 1
n = 20


def solution(a, b, n):
    answer = 0

    while n >= a:

        cock = n//a * b
        answer += cock
        last = cock + (n % a)
        n = last

        if n < a:
            break

    return answer


print(solution(a, b, n))

#  다른사람 풀이


def solution(a, b, n): return max(n - b, 0) // (a - b) * b
