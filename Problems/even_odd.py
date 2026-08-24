def count_even_odd(numbers):
    print(count_even_odd([1, 2, 3, 4, 5, 6]))  # (3, 3)
    print(count_even_odd([2, 4, 8]))  # (3, 0)
    print(count_even_odd([7]))  # (0, 1)
    print(count_even_odd([]))  # (0, 0)  ← look, an empty list that SHOULDN'T crash