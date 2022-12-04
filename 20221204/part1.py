import sys

def processData(input):
    pairs = []
    with open(input, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        line = line.split(',')
        line[0] = line[0].split('-')
        line[1] = line[1].split('-')
        pairs.append(line)
    return pairs

def main(input):
    pairs = processData(input)
    score1 = 0
    score2 = 0
    for pair in pairs:
        if ((int(pair[0][0]) <= int(pair[1][0])) and (int(pair[0][1]) >= int(pair[1][1]))) or \
        ((int(pair[1][0]) <= int(pair[0][0])) and (int(pair[1][1]) >= int(pair[0][1]))):
            score1 += 1
        if ((int(pair[0][0]) <= int(pair[1][0])) and (int(pair[0][1]) >= int(pair[1][0]))) or \
        ((int(pair[1][0]) <= int(pair[0][0])) and (int(pair[1][1]) >= int(pair[0][0]))):
            score2 += 1
    print(f'Score1: {score1}')
    print(f'Score2: {score2}')

if __name__ == "__main__":
    main(sys.argv[1])
