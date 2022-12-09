import sys

def getDirectorySize(lines, target):
    size = 0
    currentBest = None
    while len(lines) > 0:
        command = lines.pop()
        if command[:4] == '$ cd' and command.find('..') == -1:
            newSize, newBest, remainingLines = getDirectorySize(lines, target)
            size += newSize
            lines = remainingLines
            if newBest:
                if currentBest == None or newBest < currentBest:
                    currentBest = newBest
            if newSize >= target and (currentBest == None or newSize < currentBest):
                currentBest = newSize
        elif command.split()[0].isdigit():
            size += int(command.split()[0])
        elif command[:4] == '$ cd':
            return (size, currentBest, lines)
    if size >= target and (currentBest == None or size < currentBest):
        currentBest = size
    return (size, currentBest, lines)

def getTotalSize(lines):
    size = 0 
    while len(lines) > 0:
        command = lines.pop()
        if command.split()[0].isdigit():
            size += int(command.split()[0])
    return size

def main(input, target):
    with open(input, 'r') as file:
        lines = file.readlines()
    lines.reverse()
    needed = target - (70000000 - getTotalSize(lines.copy()))
    print(getDirectorySize(lines, needed)[1])


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))