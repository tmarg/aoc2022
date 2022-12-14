import sys

def makeList(string):
    l = []
    i = 0
    element = ''
    i = 1
    while i < len(string):
        if string[i] == '[':
            m , j = makeList(string[i:])
            l.append(m)
            i += j
        elif string[i].isdigit():
            element += string[i]
            i += 1
        elif string[i] == ',':
            if element != '':
                l.append(int(element))
            element = ''
            i += 1
        elif string[i] == ']':
            if element != '':
                l.append(int(element))
            i += 1
            return (l, i)

def processInput(input):
    with open(input, 'r') as file:
        lines = file.readlines()
    pairs = []
    currentPair = []
    for line in lines:
        line = line.strip()
        if line != '':
            currentPair.append(makeList(line)[0])
            if len(currentPair) == 2:
                pairs.append(currentPair)
                currentPair = []
    return pairs

def testOrder(pair):
    list1, list2 = pair
    #print((pair[0], pair[1]))
    for i in range(len(list1)):
        if i > len(list2) - 1:
            return False
        elif type(list1[i]) == int:
            if type(list2[i]) == int:
                if list1[i] < list2[i]:
                    return True
                elif list1[i] > list2[i]:
                    return False
            else:
                nextLevel = testOrder([[list1[i]], list2[i]])
                if nextLevel == True:
                    return True
                elif nextLevel == False:
                    return False
        else:
            if type(list2[i]) == int:
                nextLevel = testOrder([list1[i], [list2[i]]])
                if nextLevel == True:
                    return True
                elif nextLevel == False:
                    return False
            else:
                nextLevel = testOrder([list1[i], list2[i]])
                if nextLevel == True:
                    return True
                elif nextLevel == False:
                    return False
    if len(list1) < len(list2):
        return True
    return 'continue'

def merge(left, right):
    merged = []
    while len(left) > 0 and len(right) > 0:
        if testOrder([left[0], right[0]]):
            merged.append(left[0])
            if len(left) > 1:
                left = left[1:]
            else:
                left = []
        else:
            merged.append(right[0])
            if len(right) > 1:
                right = right[1:]
            else:
                right = []
    if len(left) > 0:
        merged += left
    if  len(right) > 0:
        merged += right
    return merged

def sort(pairs):
    if len(pairs) <= 1:
        return pairs
    mid = len(pairs) // 2
    left = sort(pairs[0:mid])
    right = sort(pairs[mid:])
    return merge(left, right)
    

def main(input):
    pairs = processInput(input)
    goodPairs = []
    for i in range(len(pairs)):
        pair = testOrder(pairs[i])
        if pair == True:
            goodPairs.append(i + 1)
    sumGoodPairs = sum(goodPairs)
    packets = []
    for pair in pairs:
        for packet in pair:
            packets.append(packet)
    packets.append([[2]])
    packets.append([[6]])
    sortedPackets = sort(packets)
    key = ((sortedPackets.index([[2]]) + 1) * (sortedPackets.index([[6]]) + 1))
    return(sumGoodPairs, key)
            
            

if __name__ == "__main__":
    print(main(sys.argv[1]))