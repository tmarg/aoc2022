import sys
import string

def processData(input):
    with open(input, 'r') as file:
        data = file.readlines()
    alphabet = set(string.ascii_uppercase)
    stacks = []
    moves = []
    for line in data:
        if line.count('[') >= 1:
            for i in range(len(line)):
                if line[i] in alphabet:
                    while len(stacks) < (i//4) + 1:
                        stacks.append([])
                    stacks[i//4].append(line[i])
        else:
            line = line.split()
            if len(line) > 1 and line[0] == 'move':
                moves.append([line[1], line[3], line[5]])
    for stack in stacks:
        stack.reverse()
    return (stacks, moves)

def main(input):
    stacks, moves = processData(input)
    for move in moves:
        for i in range(int(move[0])):
            stacks[int(move[2]) - 1 ].append(stacks[int(move[1]) - 1 ].pop())
    message = ''
    for stack in stacks:
        message += stack[-1]
    print(message)

    stacks, moves = processData(input)
    for move in moves:
        stacks[int(move[2]) - 1 ] += (stacks[int(move[1]) - 1 ][-int(move[0]):])
        stacks[int(move[1]) - 1 ] = stacks[int(move[1]) - 1][0:-int(move[0])]
    message = ''
    for stack in stacks:
        message += stack[-1]
    print(message)

if __name__ == "__main__":
    main(sys.argv[1])