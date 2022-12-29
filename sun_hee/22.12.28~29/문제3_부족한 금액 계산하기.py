# price 이용료
# N번 째 N배
# count번 탄다면??
# 얼마나 모자르는지?

price = 3
money = 20
count = 4

# 4번
# sum = 0

# for i in range(4):
#     sum += (i+1)*price

# print(sum-money)


def solution(price, money, count):
    sum = 0

    for i in range(count):
        sum += (i+1)*price

    if sum <= money:
        result = 0
    elif sum > money:
        result = sum-money

    return result


# a = [(i+1)*price for i in range(count)]

# print(sum(a))
