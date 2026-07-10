A = [1,2,3]
B = [4,5,6]

x = A.copy()

for i in B:
    x.append(i)

print("append:",x)


y = A.copy()
y.extend(B)

print("extend:",y)


print("+ operator:",A+B)