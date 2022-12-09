import sys

def main(input):
    with open(input, 'r') as file:
        lines = file.readlines()
    map = []
    visibleTrees = 0
    for line in lines:
        map.append(list(line.strip()))
    xMax = len(map[0])
    yMax = len(map)
    for y in range(yMax):
        for x in range(xMax):
            visible = False
            if y == 0 or y == (yMax -1 ):
                visible = True
            elif x == 0 or x == (xMax - 1 ):
                visible = True
            elif max(map[y][0:x]) < map[y][x] or max(map[y][x+1:xMax]) < map[y][x]:
                visible = True
            elif max([map[i][x] for i in range(0, y)]) < map[y][x] or \
                max(map[i][x] for i in range(y+1, yMax)) < map[y][x]:
                visible = True
            if visible:
                visibleTrees += 1
    print(visibleTrees)

    best = None
    bestScore = None
    for y in range(yMax):
        for x in range(xMax):
            height = map[y][x]
            upScore = 0
            downScore = 0
            leftScore = 0
            rightScore = 0
            if x > 0:
                for i in range(x - 1, -1, -1):
                    upScore += 1
                    if map[y][i] >= height:
                        break
            if x < xMax - 1:
                for i in range(x + 1, xMax):
                    downScore += 1
                    if map[y][i] >= height:
                        break
            if y > 0:
                for j in range(y - 1, -1, -1):
                    leftScore += 1
                    if map[j][x] >= height:
                        break
            if y < yMax - 1:
                for j in range(y + 1, yMax):
                    rightScore += 1
                    if map[j][x] >= height:
                        break
            score = upScore * downScore * leftScore * rightScore
            if (not best) or score > bestScore:
                best = (x, y)
                bestScore = score
    print(bestScore)     
                    



if __name__ == "__main__":
    main(sys.argv[1])
