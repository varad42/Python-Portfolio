# Q.8 A number is an Armstrong number if the sum of each digit raised to the power of the digit-count equals the number itself. E.g. 153 has 3 digits: 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✓
def armstrong_number(num):
    temp_1 = num
    temp = num
    power = 0
    result = 0
    while num != 0:
        last_digit = num%10
        num = num // 10
        power = power + 1
    while temp != 0:
        last_digit = temp % 10
        temp = temp // 10
        result = result + last_digit**power

    if result == temp_1:
        return True
    else:
        return False


print(armstrong_number(153))
print(armstrong_number(9474))
print(armstrong_number(100))
print(armstrong_number(154))
print(armstrong_number(5))




