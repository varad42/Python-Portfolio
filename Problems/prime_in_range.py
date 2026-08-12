def prime_in_range(numbers):
    for num in numbers:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)

prime_in_range(range(10, 20))

