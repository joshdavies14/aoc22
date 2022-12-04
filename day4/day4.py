f = open("in.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

fullOverlaps = 0
overlaps = 0

for line in lines:
    elf1, elf2 = line.split(",")
    elf1a, elf1b = elf1.split("-")
    elf2a, elf2b = elf2.split("-")

    task1 = list(range(int(elf1a), int(elf1b) + 1))
    task2 = list(range(int(elf2a), int(elf2b) + 1))

    # Part 1
    if all(element in task1 for element in task2) or all(element in task2 for element in task1):
        fullOverlaps += 1
    
    # Part 2
    if any(element in task1 for element in task2):
        overlaps += 1

print(fullOverlaps)
print(overlaps)