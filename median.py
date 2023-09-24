"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        if len(numbers)%2==0:
            first_mid = len(numbers)//2-1
            second_mid = first_mid + 1
            median = (numbers[first_mid] + numbers[second_mid]) / 2
        else:
            median = numbers[len(numbers)//2]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)