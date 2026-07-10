marks=[]

for i in range(10):
    marks.append(int(input("Mark: ")))

average=sum(marks)/10

count=0

for mark in marks:
    if mark>average:
        count+=1


print("Highest:",max(marks))
print("Lowest:",min(marks))
print("Average:",average)
print("Above average:",count)