# Take a 3 x 3 matrix from the user and calculate row and column sums

matrix = []

# Input matrix values
for i in range(3):
    row = list(map(int, input("Enter row values: ").split()))
    matrix.append(row)


# Calculate row sums
for row in matrix:
    print("Row sum:", sum(row))


# Calculate column sums
for column in range(3):
    total = 0

    for row in range(3):
        total += matrix[row][column]

    print("Column sum:", total)


# Calculate total matrix sum
print("Total sum:", sum(map(sum, matrix)))