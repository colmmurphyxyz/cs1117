def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum // len(numbers)


print(average(2, 3))