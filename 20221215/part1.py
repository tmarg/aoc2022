import sys

def sensorsBeacons(input):
    with open(input, 'r') as file:
        lines = file.readlines()
    pairs = []
    for line in lines:
        line = line.strip().split()
        pairs.append(((int(line[2][2:-1]), int(line[3][2:-1])), (int(line[8][2:-1]), int(line[9][2:]))))
    return pairs

def main(input, row):
    pairs = sensorsBeacons(input)
    excluded = set()
    xMin = pairs[0][0][0]
    xMax = pairs[0][0][0]
    count = 0
    for pair in pairs:
        print(count)
        count += 1
        distance = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
        for x in range(pair[0][0] - distance, pair[0][0] + distance):
            if x < xMin:
                xMin = x 
            elif x > xMax:
                xMax = x 
    count = 0
    for x in range(xMin, xMax + 1):
        print(count)
        count += 1
        for pair in pairs:
            distance = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
            if abs(pair[0][0] - x) + abs(pair[0][1] - row) <= distance:
                excluded.add((x, row))  
    count = 0
    for pair in pairs:
        print(count)
        count += 1
        if pair[1] in excluded:
            excluded.remove(pair[1])
    return len(excluded)
    
if __name__ == "__main__":
    print(main(sys.argv[1], int(sys.argv[2])))


