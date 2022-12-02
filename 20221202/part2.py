import sys

def main(input):
    score = 0 
    moves = ['A','B', 'C']
    with open(input, 'r') as file:
        rounds = file.readlines()
    for round in rounds:
        round = round.strip().split()
        if round[1] == 'X':
            score += ( ( moves.index(round[0]) + 2 )  % 3 ) + 1
        elif round[1] == 'Y':
            score += 3 + ( moves.index( round[0] ) + 1 )
        else:
            score += 6 + ( ( ( moves.index(round[0]) + 1 ) % 3 ) + 1 )
    print(score)

if __name__ == "__main__":
    main(sys.argv[1])
        