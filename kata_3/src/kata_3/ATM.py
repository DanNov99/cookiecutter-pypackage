def atm_withdrow(amount: int):
    if amount <= 0 or amount > 1500 or (amount % 10) != 0:
        return -1

    possible_banknotes = [10, 20, 50, 100, 200, 500]
    if amount in possible_banknotes:
        return 1

    counter = 0
    for banknote in reversed(possible_banknotes):
        q, mod = divmod(amount, banknote)

        counter += q
        amount = mod

    return counter
