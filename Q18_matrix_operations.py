matrix=[]

for i in range(3):
    row=list(map(int,input().split()))
    matrix.append(row)


for row in matrix:
    print("Row sum:",sum(row))


for j in range(3):
    total=0

    for i in range(3):
        total+=matrix[i][j]

    print("Column sum:",total)


print("Total:",sum(map(sum,matrix)))