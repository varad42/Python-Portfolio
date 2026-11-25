def searchMatrix(matrix , target):
    high = len(matrix) * len(matrix[0]) - 1
    low = 0
    cols =  len(matrix[0])

    while low <= high:
        mid = (low + high) // 2

        row = mid // cols
        col = mid % cols
        value = matrix[row][col]
        if target == value:
            return True
        elif target > value:
            low = mid + 1
        else:
            high = mid - 1
    return False

m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchMatrix(m, 3))      # True
print(searchMatrix(m, 13))     # False
print(searchMatrix(m, 60))     # True
print(searchMatrix([[1]], 2))  # False
print(searchMatrix([[1, 3]], 3))  # True