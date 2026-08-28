def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
    return True



    # for j in range(0,len(numbers)):
    #     for i in range(j+1, len(numbers)):
    #         if numbers[j] > numbers[i]:
    #             temp = numbers[j]
    #             numbers[j] = numbers[i]
    #             numbers[i] = temp
    # return numbers

print(is_sorted([1, 3, 7, 9]))     # True
print(is_sorted([1, 7, 3, 9]))     # False
print(is_sorted([5]))              # True
print(is_sorted([]))               # True
print(is_sorted([2, 2, 5]))        # True  ← equal neighbors allowed
