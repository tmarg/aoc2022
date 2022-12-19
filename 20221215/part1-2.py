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
    for pair in pairs:
        distance = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
        yDistance = abs(pair[0][1] - row)
        xDistance = distance - yDistance
        if xDistance >= 0:
            excluded.update(set(range(pair[0][0] - xDistance, pair[0][0] + xDistance)))    
    for pair in pairs:
        if pair[1] in excluded:
            excluded.remove(pair[1])
    return len(excluded)
    
if __name__ == "__main__":
    print(main(sys.argv[1], int(sys.argv[2])))

