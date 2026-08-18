def calaraisetob():
    base = 3
    power = 4

    while (power > 0):
        if ((power & 1) == 1):
            ans *= base

            base *= base
            power = power >> 1


    print(ans)
calaraisetob()