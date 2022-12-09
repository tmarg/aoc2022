import sys

def main(input):
    with open(input, 'r') as file:
        lines = file.readlines()

    moves = []
    for line in lines:
        move = line.strip().split()
        moves.append((move[0], int(move[1])))

    H = [0, 0]
    T = [0, 0]
    visited = set()
    for move in moves:
        for _ in range(move[1]):
            if move[0] == 'U':
                H[0] -= 1
            elif move[0] == 'D':
                H[0] += 1
            elif move[0] == 'R':
                H[1] += 1
            else:
                H[1] -= 1
            if T[0] < H[0] - 1:
                if T[1] < H[1]:
                    T[0] += 1
                    T[1] += 1
                elif T[1] > H[1]:
                    T[0] += 1
                    T[1] -= 1
                else:
                    T[0] += 1
            elif T[0] > H[0] + 1:
                if T[1] < H[1]:
                    T[0] -= 1
                    T[1] += 1
                elif T[1] > H[1]:
                    T[0] -= 1
                    T[1] -= 1
                else:
                    T[0] -= 1
            elif T[1] < H[1] - 1:
                if T[0] < H[0]:
                    T[0] += 1
                    T[1] += 1
                elif T[0] > H[0]:
                    T[0] -= 1
                    T[1] += 1
                else:
                    T[1] += 1
            elif T[1] > H[1] + 1:
                if T[0] < H[0]:
                    T[0] += 1
                    T[1] -= 1
                elif T[0] > H[0]:
                    T[0] -= 1
                    T[1] -= 1
                else:
                    T[1] -= 1
            visited.add((T[0], T[1]))
    print(len(visited))

if __name__ == "__main__":
    main(sys.argv[1])



