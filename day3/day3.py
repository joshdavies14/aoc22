import string

f = open("in.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

rucksacks = []
for line in lines:
    midpoint = len(line) // 2
    rucksacks.append((set(line[:midpoint]), set(line[midpoint:])))

priorities = list(" " + string.ascii_letters)

def character_priority(character):
    return priorities.index(character)

# Part 1
print(sum(sum(map(character_priority, a.intersection(b))) for a, b in rucksacks))

# Part 2
def getUnion(x):
    return x[0].union(x[1])

rucksacks = list(map(getUnion, rucksacks))
groups = zip(*[iter(rucksacks)] * 3)
print(sum(sum(map(character_priority, a.intersection(b).intersection(c))) for a, b, c in groups))
