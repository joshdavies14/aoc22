f = open("in.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

def uppermod(v, r):
    return v % r if v % r != 0 else r

def determineVictory(a, b):
    if a == b:
        return 3
    elif a == uppermod(b+1, 3):
        return 0    
    else:
        return 6

matches = []
for line in lines:
    opponent, move = line.split(" ")
    match opponent:
        case "A":
            opponent = 1
        case "B":
            opponent = 2
        case "C":
            opponent = 3
    match move:
        case "X":
            move = 1
        case "Y":
            move = 2
        case "Z":
            move = 3
    matches.append((opponent, move))

# Part 1
choices = sum(m[1] for m in matches)
results = sum(determineVictory(*m) for m in matches)

print(choices + results)

def determineMove(a, b):
    if b == 0:
        return uppermod(a - 1, 3)
    elif b == 6:
        return uppermod(a + 1, 3)
    else:
        return a

games = []
for line in lines:
    opponent, result = line.split(" ")
    match opponent:
        case "A":
            opponent = 1
        case "B":
            opponent = 2
        case "C":
            opponent = 3
    match result:
        case "X":
            result = 0
        case "Y":
            result = 3
        case "Z":
            result = 6
    games.append((opponent, result))

# Part 2
matches = []
matches = [(a,determineMove(a,b)) for a,b in games]
choices = sum(m[1] for m in matches)
results = sum(determineVictory(*m) for m in matches)

print(choices + results)