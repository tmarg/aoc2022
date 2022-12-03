import sys
import string

def processData(input):
    sacks = []
    with open(input, 'r') as file:
        data = file.readlines()
        for line in data:
            line = line.strip()
            sack = []
            mid = int(len(line)/2)
            sack.append(line[:mid])
            sack.append(line[mid:])
            sacks.append(sack)
    return sacks

def main(input):
    score = 0
    sacks = processData(input)
    alphabet = list(string.ascii_letters)
    priority = {}
    for i in range(len(alphabet)):
        priority[alphabet[i]] = i + 1
    for sack in sacks:
        comp1 = set(sack[0])
        comp2 = set(sack[1])
        for char in comp1:
            if char in comp2:
                score += priority[char]
                break
    print(score)

if __name__ == "__main__":
    main(sys.argv[1])