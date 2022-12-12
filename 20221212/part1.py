import sys
from queue import PriorityQueue as pq 
import string
from collections import defaultdict
class Position:
    def __init__(self, coord, end, parent=None):
        self.coord = coord
        if parent:
            self.steps = parent.getSteps() + 1
        else:
            self.steps = 0
        self.priority = abs(end[0] - self.coord[0]) + abs(end[1] - self.coord[1]) + self.steps
    def __lt__(self, other):
        return self.priority < other.priority
    def __gt__(self, other):
        return self.priority > other.priority
    def __eq__(self, other):
        return self.priority == other.priority
    def getPriority(self):
        return self.priority
    def getSteps(self):
        return self.steps
    def getCoord(self):
        return self.coord

def processMap1(input):
    with open(input, 'r') as file:
        lines = file.readlines()
    map = [line.strip() for line in lines]
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 'S':
                start = (y, x)
            elif map[y][x] == 'E':
                end = (y, x)
    return (map, start, end)

def processMap2(input):
    with open(input, 'r') as file:
        lines = file.readlines()
    map = [line.strip() for line in lines]
    starts = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 'S' or map[y][x] == 'a':
                starts.append((y, x))
            elif map[y][x] == 'E':
                end = (y, x)
    return (map, starts, end)
    
    
    
def countSteps(map, start, end):
    alphabet = list(string.ascii_lowercase)
    height = {}
    for i in range(len(alphabet)):
        height[alphabet[i]] = i 
    height['S'] = 0
    height['E'] = 25
    searched = defaultdict(lambda: float('inf'))
    queue = pq(0)
    queue.put(Position(start, end))
    while queue.empty() == False:
        pos = queue.get()
        if pos.getCoord() == end:
            return pos.getSteps()
        else:
            y, x = pos.getCoord()
            if y > 0:
                if height[map[y-1][x]] <= height[map[y][x]] + 1:
                    child = Position((y - 1, x), end, pos)
                    if searched[child.getCoord()] > child.getPriority():
                        searched[child.getCoord()] = child.getPriority()
                        queue.put(child)
            if y < len(map) - 1:
                if height[map[y+1][x]] <= height[map[y][x]] + 1:
                    child = Position((y + 1, x), end, pos)
                    if searched[child.getCoord()] > child.getPriority():
                        searched[child.getCoord()] = child.getPriority()
                        queue.put(child)
            if x > 0:
                if height[map[y][x-1]] <= height[map[y][x]] + 1:
                    child = Position((y, x - 1), end, pos)
                    if searched[child.getCoord()] > child.getPriority():
                        searched[child.getCoord()] = child.getPriority()
                        queue.put(child)
            if x < len(map[0]) - 1:
                if height[map[y][x+1]] <= height[map[y][x]] + 1:
                    child = Position((y, x + 1), end, pos)
                    if searched[child.getCoord()] > child.getPriority():
                        searched[child.getCoord()] = child.getPriority()
                        queue.put(child)
    #print("Path not found!")

def main(input):
    map, start, end = processMap1(input)
    part1 = countSteps(map, start, end)
    map, starts, end = processMap2(input)
    routes = []
    for start in starts:
        route = countSteps(map, start, end)
        if route:
            routes.append(route)
    routes.sort()
    part2 = routes[0]
    return (part1, part2)

if __name__ == "__main__":
    print(main(sys.argv[1]))


    
