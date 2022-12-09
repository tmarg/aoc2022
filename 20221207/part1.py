import sys

def processData(input):
    with open(input, 'r') as file:
        lines = file.readlines()
    return lines 

def getDirectorySize(lines, target):
    size = 0
    foundDirectories = []
    while len(lines) > 0:
        command = lines.pop()
        if command[:4] == '$ cd' and command.find('..') == -1:
            newSize, newDirectories, remainingLines = getDirectorySize(lines, target)
            size += newSize
            foundDirectories += newDirectories
            lines = remainingLines
            if newSize <= target:
                foundDirectories.append(newSize)
        elif command.split()[0].isdigit():
            size += int(command.split()[0])
        elif command[:4] == '$ cd':
            return (size, foundDirectories, lines)
    if size <= target:
        foundDirectories.append(size)
    return (size, foundDirectories, lines)

def main(input, target):
    lines = processData(input)
    lines.reverse()
    print(sum(getDirectorySize(lines, target)[1]))


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))