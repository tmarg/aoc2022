import sys

def processData(input):
    with open(input, 'r') as file:
        data = file.readlines()
        packet = ''
        for line in data:
            line = line.strip()
            packet += line
        return packet

def main(input):
    packet = processData(input)
    for i in range(3,len(packet)):
        if len(set(packet[i-3:i+1])) == 4:
            print(f"Part1: {i + 1}")
            break
    for i in range(13,len(packet)):
        if len(set(packet[i-13:i+1])) == 14:
            print(f"Part2: {i + 1}")
            break
    
if __name__ == "__main__":
    main(sys.argv[1])