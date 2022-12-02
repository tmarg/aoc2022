import sys

def main(input):
    score = 0
    moves = ['A', 'B', 'C']
    with open(input, 'r') as file:
        rounds = file.readlines()
    for round in rounds:
        round = round.strip().split()
        if round[1] == 'X':
            round[1] = 'A'
        elif round[1] == 'Y':
            round[1] = 'B'
        else:
            round[1] = 'C'
        if round[0] == round[1]:
            score += 3
        elif round[1] == moves[(moves.index(round[0]) + 1) % 3]:
            score += 6
        if round[1] == 'A':
            score += 1
        elif round[1] == 'B':
            score += 2
        else:
            score += 3
    print(score)

if __name__ == "__main__":
    main(sys.argv[1])
        

