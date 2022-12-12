import sys
import math

class Monkey:
    def __init__(self, items, operation, test, monkeyList):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0
        self.monkeyList = monkeyList
        self.mod = None
    def inspect(self):
        if not self.mod:
            self.mod = math.prod([monkey.test[0] for monkey in self.monkeyList])
        for i in range(len(self.items)):
            self.inspections += 1
            if self.operation[0] == '+':
                self.items[i] += int(self.operation[1])
            elif self.operation[0] == '*':
                if self.operation[1] == 'old':
                    self.items[i] = self.items[i] * self.items[i]
                else:
                    self.items[i] *= int(self.operation[1])
            self.items[i] = self.items[i] % self.mod
    def testItems(self):
        while len(self.items) > 0:
            item = self.items.pop()
            if item % self.test[0] == 0:
                self.monkeyList[self.test[1]].receive(item)
            else:
                self.monkeyList[self.test[2]].receive(item)
    def receive(self, item):
        self.items.append(item)
    def takeTurn(self):
        self.inspect()
        self.testItems()

def processInput(input):
    with open(input, 'r') as file:
        lines = file.readlines()
    monkeys = []
    monkey = []
    monkeyTest = []
    for i in range(len(lines)):
        line = lines[i].strip()
        if i % 7 == 1:
            items = []
            line[15:].split()
            for item in line[15:].split():
                items.append(int(item.strip(', ')))
            monkey.append(items)
        if i % 7 == 2:
            line = line.split()
            monkey.append([line[-2], line[-1]])
        if i % 7 == 3:
            monkeyTest.append(int(line.split()[-1]))
        if i % 7 == 4:
            monkeyTest.append(int(line.split()[-1]))
        if i % 7 == 5:
            monkeyTest.append(int(line.split()[-1]))
            monkey.append(monkeyTest)
            monkeys.append(Monkey(monkey[0], monkey[1], monkey[2], monkeys))
            monkeyTest = []
            monkey = []
    return monkeys

def main(input):
    monkeys = processInput(input)
    for i in range(10000):
        for monkey in monkeys:
            monkey.takeTurn()
    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort()
    print(inspections[-1] * inspections[-2])
 



if __name__ == "__main__":
    main(sys.argv[1])