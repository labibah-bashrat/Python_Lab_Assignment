runs=[
45,67,100,20,55,
88,120,30,70,10,
50,90,110,40,75
]

print("Total:",sum(runs))
print("Average:",sum(runs)/len(runs))
print("Highest:",max(runs))
print("Lowest:",min(runs))


half=0
century=0

for score in runs:
    if score>=50:
        half+=1

    if score>=100:
        century+=1


print("Half centuries:",half)
print("Centuries:",century)