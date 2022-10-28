def total(pocket):
    pocket_sum = 0

    for i in pocket:
        pocket_sum += i*pocket[i]

    return pocket_sum


def take(pocket, money_in):
    for i in money_in:
        if i in pocket:
            pocket[i] += money_in[i]
        else:
            pocket[i] = money_in[i]


def pay(pocket, amt):
    bank = []

    for i in pocket:
        bank.append(i)

    bank.sort(reverse=True)
    used = {}

    for i in bank:
        if amt > i:
            n = amt//i
            if n > pocket[i]:
                n = pocket[i]
            used[i] = n
            amt -= n*i

    if amt != 0:
        return {}

    for i in used:
        pocket[i] -= used[i]

    return used


exec(input().strip())
