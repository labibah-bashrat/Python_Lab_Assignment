# Take a 3 x 3 matrix from the user and calculate row and column sums

matrix = []

for i in range(3):
    row = list(map(int, input("Enter 3 values for row: ").split()))

    while len(row) != 3:
        print("Please enter exactly 3 values.")
        row = list(map(int, input("Enter 3 values for row: ").split()))

    matrix.append(row)


print("Row sums:")

for row in matrix:
    print(sum(row))


print("Column sums:")

for column in range(3):
    total = 0

    for row in range(3):
        total += matrix[row][column]

    print(total)


print("Total sum:", sum(map(sum, matrix)))