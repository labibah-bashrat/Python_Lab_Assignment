# Take a 3 x 3 matrix from the user and calculate row and column sums

matrix = []

# Input matrix values
for i in range(3):
    row = list(map(int, input("Enter 3 values separated by spaces: ").split()))

    while len(row) != 3:
        print("Please enter exactly 3 numbers separated by spaces.")
        row = list(map(int, input("Enter 3 values separated by spaces: ").split()))

    matrix.append(row)


# Calculate row sums
print("Row sums:")

for row in matrix:
    print(sum(row))


# Calculate column sums
print("Column sums:")

for column in range(3):
    total = 0

    for row in range(3):
        total += matrix[row][column]

    print(total)


# Calculate total sum
print("Total sum:", sum(map(sum, matrix)))