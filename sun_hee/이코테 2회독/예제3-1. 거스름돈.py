# 500원, 100원, 50원, 10원 무한히 존재함
# 거슬러줘야 할 동전의 최소 개수는?
# 거슬러 줘야 할 돈 N은 항상 10의 배수

# change = [500, 100, 50, 10]

# 내 답안 :  이중반복문으로 효율적이지 않다!

# N = int(input())

# n = 0 # 거슬러준 횟수

# for coin in change:
#     while N >= coin:
#         N = N - coin
#         n = n + 1
#         if N < coin:
#             break
# print(n)
 
# -------------------------------------

change = [500, 100, 50, 10]

N = int(input())

n = 0

for coin in change:
    n = n + N // coin
    N = N % coin

print(n)