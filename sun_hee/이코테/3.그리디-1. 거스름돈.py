# 거스름돈 문제

# print(money//coin[0])
# print(money-money//coin[0]*coin[0])
# money = money-money//coin[0]*coin[0]
# print(money//coin[1])
# print(money-money//coin[1]*coin[1])
# money = money-money//coin[1]*coin[1]
# print(money//coin[2])
# print(money-money//coin[2]*coin[2])
# money = money-money//coin[2]*coin[2]
# print(money//coin[3])
# print(money-money//coin[3]*coin[3])

money = 870


def coin(money):
    coins = [500, 100, 50, 10]

    sum = 0
    for i in range(len(coins)):
        cnt = money//coins[i]
        sum += cnt
        money -= cnt*coins[i]
    return sum


print(coin(money))

# -----------------------------------------
# 엘리스 답


def coins(n):
    # 동전 종류가 주어집니다.
    coins = [10, 50, 100, 500]
    coins.sort(reverse=True)

    # 각각의 동전이 필요한 개수를 초기화해요.
    result = {x: 0 for x in coins}

    for coin in coins:
        # 각 동전이 사용되는 개수를 저장해 주세요. (힌트: 나눗셈의 몫 활용)
        coinCount = n // coin

        # 동전으로 거스르고 남은 금액을 갱신해 주세요.
        n -= coinCount * coin

        result[coin] = coinCount

    return result


def main():
    n = int(input())
    cnt = 0
    for value in coins(n).values():
        cnt += value
    print(cnt)


if __name__ == "__main__":
    main()
