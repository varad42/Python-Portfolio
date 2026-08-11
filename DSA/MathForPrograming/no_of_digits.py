import math
def no_of_digits():
    n = 34567
    base = 10
    ans = int(math.log(n) / math.log(base) + 1)
    print(ans)

no_of_digits()