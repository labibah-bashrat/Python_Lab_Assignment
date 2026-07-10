numbers = [5,10,15,20,25]

target = int(input("Enter number: "))

if target in numbers:
    print("Found at index:", numbers.index(target))
else:
    print("Not found")