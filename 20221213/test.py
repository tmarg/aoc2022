from part1 import makeList
from part1 import processInput
from part1 import testOrder
from part1 import merge
from part1 import sort



#print(makeList('[1,1,3,1,1]'))
#print(makeList('[[[4,[7],[1,1,4,3,8],[3],[]],[[5,10,2,1],9,[2],6,7],4,[],[[10],[6,3,1,7]]],[4,[6],[[6],[6,6]]],[[[0,2,5],[3,5,10,7],[10,7,2,9],[],[0]],[[9,9,8],[]],[10,[2,10,7,7,3],4],[2,7]]]'))

#print(testOrder([[[]],[[[5,4],5]]]))
#print([].reverse())
packets = []
x = processInput('testinput.txt')
for pair in x:
    for packet in pair:
        packets.append(packet)
packets.append([[2]])
packets.append([[6]])
y = sort(packets)
for packet in y:
    print(packet)