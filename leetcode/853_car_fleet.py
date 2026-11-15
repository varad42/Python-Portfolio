# Complexity: O(n log n) time. The loop is O(n), but sorted costs O(n log n), and the bigger one wins. Space is O(n), for cars and the stack.

def carFleet(target, positon, speed):
    cars = list(zip(positon, speed))
    cars = sorted(cars, reverse=True)
    stack = []

    for position,speed in cars:
        current_car_time = (target - position) / speed
        if len(stack) == 0 or current_car_time > stack[-1]:
            stack.append(current_car_time)

    return len(stack)

print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))   # 3
print(carFleet(10, [3], [3]))                    # 1
print(carFleet(100, [0,2,4], [4,2,1]))           # 1