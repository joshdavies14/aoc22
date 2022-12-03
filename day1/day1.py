f = open("in.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

elves = [0]
for line in lines:
    if line == "":
        # New elf - add a new entry to the list
        elves.append(0)
    else:
        # Get last element in array and add value to it
        elves[-1] += int(line)
elves.pop(0)

# Part 1
print(max(elves))

# Part 2
print(sum(sorted(elves)[-3:]))