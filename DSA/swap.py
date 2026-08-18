numbers = [1,2,3,4]
def swap(arr,index_number1,index_number2):
    temp = arr[index_number1]
    arr[index_number1] = arr[index_number2]
    arr[index_number2] = temp
    return arr


print(swap(numbers,3,2))