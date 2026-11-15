def threeSum(numbers):
    numbers = sorted(numbers)
    result = []

    for i in range(len(numbers)):
        if i > 0 and numbers[i] == numbers[i-1]:
            continue
        target = -numbers[i]
        left = i+1
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                result.append([numbers[i], numbers[left],numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))   # [[-1, -1, 2], [-1, 0, 1]]
print(threeSum([0, 0, 0, 0]))            # [[0, 0, 0]]
print(threeSum([1, 2, 3]))               # []
print(threeSum([-2, 0, 0, 2, 2]))        # [[-2, 0, 2]]