# Create and analyze a 3 x 3 matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
print(matrix)

# Print first row
print("First row:", matrix[0])

# Extract last column
last_column = []

for row in matrix:
    last_column.append(row[-1])

print("Last column:", last_column)


# Calculate total sum of matrix elements
total = 0

for row in matrix:
    for value in row:
        total += value

print("Sum of all elements:", total)