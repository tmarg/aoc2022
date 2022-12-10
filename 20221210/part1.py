import sys

def main(input):
    with open(input, 'r') as file:
        commands = [line.strip().split() for line in file.readlines()]
    signalStrengths = {}
    commandCycles = {'noop': 1, 'addx': 2}
    cycles = 0
    X = 1
    signalSum = None
    message = ''
    for command in commands:
        if abs(X - (cycles % 40)) <= 1:
            message += '#'
        else:
            message += '.'
        if command[0] == 'addx':
            if abs(X - ((cycles + 1) % 40)) <=1:
                message += '#'
            else:
                message += '.'
        record = (cycles - 20) // 40
        cycles += commandCycles[command[0]]
        newRecord = (cycles - 20) // 40
        if newRecord > record:
            signalStrengths[(newRecord * 40) + 20] = ((newRecord * 40) + 20) * X
        if len(command) == 2:
            X += int(command[1])
        if len(list(signalStrengths)) == 6:
            signalSum = sum(signalStrengths.values())
    
    print(signalSum)
    line = ''
    for i in range(len(message)):
        line += message[i]
        if len(line) == 40:
            print(line)
            line = ''
        



if __name__ == "__main__":
    main(sys.argv[1])

            
        