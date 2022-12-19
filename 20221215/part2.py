import sys
from part1 import sensorsBeacons

def main(input, size):
    pairs = sensorsBeacons(input)
    exclude = []
    for y in range(size):
        if y % 100000 == 0:
            print(y)
        exclude = []
        for pair in pairs:
            distance = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
            yDistance = abs(pair[0][1] - y)
            xDistance = distance - yDistance
            if xDistance >= 0:
                exclude.append([pair[0][0] - xDistance, pair[0][0] + xDistance])
        exclude.sort(key=lambda x: x[0])
        minExclude = exclude[0]
        for i in range(len(exclude)):
            #print(minExclude)
            #print(exclude[i])
            if exclude[i][0] <= minExclude[1] and exclude[i][1] >= minExclude[1]:
                minExclude[1] = exclude[i][1]
            #print(minExclude)
        #print(minExclude, size)
        if minExclude[0] > 0 or minExclude[1] < size:
            if minExclude[0] > 0:
                return y + (minExclude[0] - 1) * 4000000
            elif minExclude[1] < size:
                return y + (minExclude[1] + 1) * 4000000
            


if __name__ == "__main__":
    print(main(sys.argv[1], int(sys.argv[2])))