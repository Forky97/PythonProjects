def combination_change(money: int, coins: list) -> int:
    comb = [1] + ([0] * (money + 1))

    for coin in coins:

        for i in range(coin, money + 1):
            comb[i] += comb[i - coin]

    return comb[money]


print(combination_change(10, [2, 1, 5, 6]))
