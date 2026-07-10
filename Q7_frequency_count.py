# Count the frequency of each element in a list

numbers = [1, 2, 2, 3, 1, 1]

frequency = {}

# Store element count in dictionary
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Display frequency
for key, value in frequency.items():
    print(key, "->", value)