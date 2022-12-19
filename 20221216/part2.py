import sys
from queue import Queue
from part1 import graph

def main(input):
    nodes = graph(input)
    totalValue = [v[0] for v in nodes.values() if v[0] > 0]
    totalValue.sort(reverse=True)
    valveCount = sum([1 for v in nodes.values() if v[0] > 0])
    currentNode1 = 'AA'
    currentNode2 = 'AA'
    path1 = ['AA']
    path2 = ['AA']
    queue = Queue()
    bestScore = 0
    bestPaths = None
    #[[Room1, Room2], [path1], [path2], set(opened), time, score, outstandingValue]
    #path = [room label or 'open']
    queue.put([['AA', 'AA'], path1, path2, set(), 26, 0, totalValue])
    while not queue.empty():
        state = queue.get()
        label1 = state[0][0]
        label2 = state[0][1]
        path1 = state[1]
        path2 = state[2]
        opened = state[3]
        valveStatus1 = label1 in opened
        valveStatus2 = label2 in opened
        time = state[4]
        score = state[5]
        valveValue1 = nodes[label1][0]
        valveValue2 = nodes[label2][0]
        poss1 = valveValue1 > 0 and label1 not in opened
        poss2 = valveValue2 > 0 and label2 not in opened
        possibleScore = 0
        outstandingValue = state[6]
        i = 0
        if poss1 or poss2:
            tt = time
        else:
            tt = time - 1
        for t in range(tt - 1, 0, -2):
            if i < (len(outstandingValue)):
                possibleScore += t * outstandingValue[i]
            if i + 1 < len(outstandingValue) and (poss1 and poss2):
                possibleScore += t * outstandingValue[i + 1]

        if score > bestScore:
            bestScore = score
            bestPath = (path1, path2)
            print(score)
            print(path1)
            print(path2)
            print(queue.qsize())
            #print(time)
        exs1 = nodes[label1][1]
        exs2 = nodes[label2][1]
        if time > 1 and len(state[3]) < valveCount and score + possibleScore > bestScore:
            options1 = []
            options2 = []
            if valveStatus1 == False and valveValue1 > 0:
                options1.append('open')
            if valveStatus2 == False and valveValue2 > 0 and label1 != label2:
                options2.append('open')
            for ex in exs1:
                #only visit room if we haven't been there or we've opened a valve since being there before
                rev1 = list(reversed(path1))
                if path1.count(ex) == 0 or (path1.count('open') >= 1 and rev1.index('open') < rev1.index(ex)) and rev1[rev1.index('open') + 1] != ex:
                    options1.append(ex)
            for ex in exs2:
                rev2 = list(reversed(path2))
                if path2.count(ex) == 0 or (path2.count('open') >= 1 and rev2.index('open') < rev2.index(ex)) and rev2[rev2.index('open') + 1] != ex:
                    options2.append(ex)
            statusChoices = []
            if len(options1) == 0:
                options2.append(label1)
            if len(options2) == 0:
                options2.append(label2)
            for option1 in options1:
                for option2 in options2:
                    newpath1 = path1.copy()
                    newpath2 = path2.copy()
                    newOV = outstandingValue.copy()
                    newOpened = opened.copy()
                    newScore = score
                    newpath1 += [option1]
                    newpath2 += [option2]
                    if option1 == 'open':
                        newOV.remove(valveValue1)
                        newOpened.add(label1)
                        newScore += valveValue1 * (time - 1)
                        option1 = label1
                    if option2 == 'open':
                        newOV.remove(valveValue2)
                        newOpened.add(label2)
                        newScore += valveValue2 * (time - 1)
                        option2 = label2
                    statusChoices.append(([option1, option2], newpath1, newpath2, newOpened, time - 1,  newScore, newOV))
            for choice in statusChoices:
                queue.put(choice)
    return (bestScore, bestPath)

if __name__ == "__main__":
    print(main(sys.argv[1]))
                    






