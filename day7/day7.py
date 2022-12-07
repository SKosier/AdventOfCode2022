from enum import Enum


class Command(Enum):
    command = "$"
    cd = "cd"
    list = "ls"


class Node:
    def __init__(self, name, isDir, parent=None, size=None):
        self.name = name
        self.size = size
        self.isDir = isDir
        self.parent = parent
        if self.isDir:
            self.subElems = {}

    def insert(self, elemName, size):
        subElem = Node(elemName, True, self)
        if size.isnumeric():
            subElem = Node(elemName, False, self, int(size))
        self.subElems[elemName] = subElem


def getHeadDir(currentDir):
    if currentDir.parent is None:
        return currentDir
    return getHeadDir(currentDir.parent)


def positionItself(currentDir, param):
    match param:
        case "..":
            return currentDir.parent
        case "/":
            return getHeadDir(currentDir)
        case _:
            return currentDir.subElems[param]


def constructHierarchy(home, lines):
    currentDir = home
    currentCommand = Command
    for i in range(0, len(lines)):
        if lines[i].startswith("$"):
            fields = lines[i].split()
            # take the executed command
            match fields[1]:
                case "cd":
                    currentDir = positionItself(currentDir, fields[2])
                case "ls":
                    currentCommand = Command.list
        else:
            # for now it means currentCommand = Command.list
            data = lines[i].split()
            currentDir.insert(data[1], data[0])


def calculateSizes(current):
    sum = 0
    for name, item in current.subElems.items():
        if item.isDir:
            calculateSizes(item)
        sum += item.size
    current.size = sum


def getAllUnderLimit(currentDir, limit):
    sum = 0
    if currentDir.size <= limit:
        sum += currentDir.size

    for name, item in currentDir.subElems.items():
        if item.isDir:
            sum += getAllUnderLimit(item, limit)

    return sum


def findMinimalBiggerThan(currentDir, needToFree, currentMin):
    if currentMin > currentDir.size >= needToFree:
        currentMin = currentDir.size

    for name, item in currentDir.subElems.items():
        if item.isDir:
            min = findMinimalBiggerThan(item, needToFree, currentMin)
            if min < currentMin:
                currentMin = min

    return currentMin


def findOneToDelete(home, total, needed):
    unused = total - home.size
    needToFree = needed - unused

    return findMinimalBiggerThan(home, needToFree, home.size)


if __name__ == '__main__':
    f = open('day7_input.txt', 'r')
    lines = f.readlines()

    home = Node("/", True)
    constructHierarchy(home, lines)
    calculateSizes(home)

    print(getAllUnderLimit(home, 100000))
    print(findOneToDelete(home, 70000000, 30000000))
