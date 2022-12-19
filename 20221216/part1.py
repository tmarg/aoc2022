import sys
from queue import Queue

def graph(input):
    with open(input, 'r') as file:
        lines = file.readlines()
    nodes = {}
    for line in lines:
        line = line.strip().split()
        connections = [i.strip(',') for i in line[9:]]
        nodes[line[1]] = [int(line[4][5:-1]), tuple(connections)]
    return nodes

def main(input):
    nodes = graph(input)
    totalValue = [v[0] for v in nodes.values() if v[0] > 0]
    totalValue.sort(reverse=True)
    valveCount = sum([1 for v in nodes.values() if v[0] > 0])
    print(totalValue)
    print(valveCount)
    currentNode = 'AA'
    path = []
    queue = Queue()
    bestScore = 0
    bestPath = None
    #[room, [path], time, score]
    #path = [room label or open]
    queue.put(['AA', [], 30, 0, totalValue])
    while not queue.empty():
        currentRoom = queue.get()
        label = currentRoom[0]
        path = currentRoom[1]
        valveStatus = 'closed'
        time = currentRoom[2]
        outstandingValue = currentRoom[4].copy()
        possibleScore = 0
        i = 0
        for t in range(time -1, 0, -2):
            if i < len(outstandingValue):
                possibleScore += t * outstandingValue[i]
                i += 1
            else:
                break
        for i, v in enumerate(path):
            if v == label and i < len(path) - 1:
                if path[i + 1] == 'open':
                    valveStatus = 'opened'
        valveValue = nodes[label][0]
        score = currentRoom[3]
        if score > bestScore:
            bestScore = score
            bestPath = path
            print(score)
            print(path)
            print(queue.qsize())
        exs = nodes[label][1]
        if time > 1 and path.count('open') < valveCount:
            options = []
            if valveStatus == 'closed' and valveValue > 0 and score + possibleScore > bestScore:
                newOV = outstandingValue.copy()
                newOV.remove(valveValue)
                options.append([label, path + ['open'], time -1, score + (valveValue * (time-1)), newOV])
            for ex in exs:
                #only visit room if we haven't been there or we've opened a valve since being there before
                if path.count(ex) == 0 or (path.count('open') >= 1 and list(reversed(path)).index('open') < list(reversed(path)).index(ex)):
                    if score + possibleScore > bestScore:
                        options.append([ex, path + [ex], time -1, score, outstandingValue])
            for option in options:
                queue.put(option)
    return (bestScore, bestPath)


if __name__ == "__main__":
    result = main(sys.argv[1])
    print(result[0])
    print(result[1])


