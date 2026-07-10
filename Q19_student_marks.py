# Analyze marks of 10 students

marks = []

# Store student marks
for i in range(10):
    mark = int(input("Enter mark: "))
    marks.append(mark)


average = sum(marks) / len(marks)

above_average = 0

# Count students scoring above average
for mark in marks:
    if mark > average:
        above_average += 1


print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Average mark:", average)
print("Students above average:", above_average)