import sys

def processData(input):
    elves = []
    with open(input, 'r') as file:
        data = file.readlines()
    current = []
    for line in data:
        line = line.strip()
        if line != '':
            current.append(int(line))
        else:
            elves.append(current.copy())
            current = []
    elves.append(current.copy())
    return elves

def main(input):
    elves = processData(input)
    for i in range(len(elves)):
        elves[i] = sum(elves[i])
    print((max(elves), elves.index(max(elves)) + 1 ))
    elves.sort()
    totalTopThree = 0
    for i in range(3):
        totalTopThree += elves.pop()
    print(totalTopThree)

if __name__ == "__main__":
    main(sys.argv[1])
