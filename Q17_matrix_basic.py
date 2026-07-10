matrix=[
[1,2,3],
[4,5,6],
[7,8,9]
]

print(matrix)

print("First row:",matrix[0])

column=[]

for row in matrix:
    column.append(row[-1])

print("Last column:",column)


total=0

for row in matrix:
    for value in row:
        total+=value

print("Sum:",total)