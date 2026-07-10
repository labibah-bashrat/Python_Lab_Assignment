# Q2_input_append.py – Take 10 integers from the user and store in a list

numbers = []

# Prompt the user for 10 integers
for i in range(10):
    value = int(input(f"Enter integer {i+1}: "))
    numbers.append(value)

# Print the complete list and total number of elements
print("List:", numbers)
print("Total elements:", len(numbers))