import part1

rockMap = part1.makeMap('testinput.txt')
for rock in rockMap:
    toprint = ''
    for i in range(len(rock)):
        toprint += rock[i]
    print(toprint)
minX = 494
maxY = 9
for _ in range(25):
    print(part1.dropSand(rockMap, minX, maxY))
    for rock in rockMap:
        toprint = ''
        for i in range(len(rock)):
            toprint += rock[i]
        print(toprint)