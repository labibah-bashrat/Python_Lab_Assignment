# Analyze cricket performance statistics

runs = [
    45, 67, 100, 20, 55,
    88, 120, 30, 70, 10,
    50, 90, 110, 40, 75
]


# Basic performance calculations
print("Total runs:", sum(runs))
print("Average runs:", sum(runs) / len(runs))
print("Highest score:", max(runs))
print("Lowest score:", min(runs))


half_centuries = 0
centuries = 0


# Count half-centuries and centuries
for score in runs:
    if score >= 50:
        half_centuries += 1

    if score >= 100:
        centuries += 1


print("Number of half-centuries:", half_centuries)
print("Number of centuries:", centuries)