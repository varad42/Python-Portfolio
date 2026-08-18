numbers = [1,2,3,4,2]
def maximum_number(numbers):
    max_item = 0

    for i in numbers:
        if max_item <= i:
            max_item = i
    return max_item
print(maximum_number(numbers))