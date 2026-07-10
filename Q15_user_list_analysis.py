# Take a list of integers from the user and calculate statistics

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Largest value:", max(numbers))
print("Smallest value:", min(numbers))