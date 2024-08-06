def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average


numbers = [2, 4, 15, 35]

result = calculate_average(numbers)
print(f"The average of the numbers is {result}")



