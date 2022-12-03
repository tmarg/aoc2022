import sys
import string
from part1 import processData

def main(input):
    score = 0
    sacks = processData(input)
    alphabet = list(string.ascii_letters)
    priority = {}
    for i in range(len(alphabet)):
        priority[alphabet[i]] = i + 1
    groups = []
    group = []
    count = 0
    for i in range(len(sacks)):
        count += 1
        sack = set(sacks[i][0]).union(set(sacks[i][1]))
        group.append(sack)
        if count >= 3:
            groups.append(group)
            group = []
            count = 0
    for group in groups:
        for char in ((group[0] & group[1]) & group[2]):
            score += priority[char]
    print(score)

if __name__ == "__main__":
    main(sys.argv[1])

        
        