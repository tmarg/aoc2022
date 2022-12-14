import sys

def makeMap(input):
    with open(input, 'r') as file:
        lines = file.readlines()
    rocks = []
    for line in lines:
        line = line.strip()
        rock = line.split(' -> ')
        for i in range(len(rock)):
            segment = rock[i]
            segment = segment.split(',')
            for j in range(2):
                segment[j] = int(segment[j])
            rock[i] = segment
        rocks.append(rock)
    maxX = 0
    minX = 500
    maxY = 0
    for rock in rocks:
        for segment in rock:
            if segment[0] > maxX:
                maxX = segment[0]
            elif segment[0] < minX:
                minX = segment[0]
            if segment[1] > maxY:
                maxY = segment[1]
    rockMap = []
    for i in range(maxY + 2):
        rockMap.append(['.' for j in range(maxX + 1 - minX)])
    for rock in rocks:
        for i in range(1,len(rock)):
            if rock[i][0] == rock[i - 1][0]:
                for j in range(min([rock[i-1][1], rock[i][1]]), max([rock[i-1][1], rock[i][1]]) + 1):
                    rockMap[j][rock[i][0] - minX] = '#'
            elif rock[i][1] == rock[i - 1][1]:
                for j in range(min([rock[i-1][0], rock[i][0]]), max([rock[i-1][0], rock[i][0]]) + 1):
                    rockMap[rock[i][1]][j - minX] = '#'
    return (rockMap, minX, maxY)

def dropSand(rockMap, minX, maxY):
    blocked = False
    location = (0, 500 - minX)
    while not blocked:
        if location[0] > maxY:
            return 'END'
        if rockMap[location[0] + 1][location[1]] == '.':
            location = (location[0] + 1, location[1])
        elif rockMap[location[0] + 1][location[1] - 1] == '.':
            location = (location[0] + 1, location[1] - 1)
        elif rockMap[location[0] + 1][location[1] + 1] == '.':
            location = (location[0] + 1, location[1] + 1)
        else:
            blocked = True
    rockMap[location[0]][location[1]] = 'o'

def main(input):
    rockMap, minX, maxY = makeMap(input)
    sandCount = 0
    while True:
        sandCount += 1
        if dropSand(rockMap, minX, maxY) == 'END':
            return sandCount - 1

if __name__ == "__main__":
    print(main(sys.argv[1]))
    


