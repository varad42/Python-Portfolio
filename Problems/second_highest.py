def second_largest(numbers):
    if len(numbers) < 2:
        raise ValueError("need at least 2 elements to find a second largest")
    elif numbers[0] > numbers[1]:
        large_num = numbers[0]
        sec_large_num = numbers[1]
    else:
        large_num = numbers[1]
        sec_large_num = numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] > large_num:
            sec_large_num = large_num
            large_num = numbers[i]
        elif numbers[i] > sec_large_num:
            sec_large_num = numbers[i]

    return sec_large_num
print(second_largest([10, 5, 8, 20, 3])) 
print(second_largest([20, 10]))
print(second_largest([5, 20, 20, 3]))
print(second_largest([7]))