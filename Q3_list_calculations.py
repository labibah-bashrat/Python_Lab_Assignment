# Calculate sum, average, maximum and minimum without using built-in functions

numbers = [10, 20, 5, 40, 15]

total = 0
maximum = numbers[0]
minimum = numbers[0]

# Traverse the list and calculate required values
for num in numbers:
    total += num

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

average = total / len(numbers)

print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)