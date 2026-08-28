def dedupe(numbers):
    unique_elements = []
    for i in numbers:
        if i in unique_elements:
            continue
        else:
            unique_elements.append(i)

    return unique_elements


print(dedupe([1, 3, 1, 5, 3]))    # [1, 3, 5]
print(dedupe([7, 7, 7, 7]))       # [7]
print(dedupe([1, 2, 3]))          # [1, 2, 3]
print(dedupe([]))                 # []