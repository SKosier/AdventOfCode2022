def isContained(firstPair, secondPair):
    if firstPair[0] <= secondPair[0] <= firstPair[1] and firstPair[0] <= secondPair[1] <= firstPair[1]:
        return True
    if secondPair[0] <= firstPair[0] <= secondPair[1] and secondPair[0] <= firstPair[1] <= secondPair[1]:
        return True
    return False


def isOverlap(firstPair, secondPair):
    if secondPair[1] >= firstPair[1] >= secondPair[0] or firstPair[1] >= secondPair[1] >= firstPair[0]:
        return True
    if secondPair[1] >= firstPair[0] >= secondPair[0] or firstPair[1] >= secondPair[0] >= firstPair[0]:
        return True
    return isContained(firstPair, secondPair)


def fullyContainedPairs(lines):
    sum = 0
    for l in lines:
        firstPair = l.strip().split(',')[0].split('-')
        secondPair = l.strip().split(',')[1].split('-')
        if isContained([eval(i) for i in firstPair], [eval(i) for i in secondPair]):
            sum += 1
    return sum


def overlappingPairs(lines):
    sum = 0
    for l in lines:
        firstPair = l.strip().split(',')[0].split('-')
        secondPair = l.strip().split(',')[1].split('-')
        if isOverlap([eval(i) for i in firstPair], [eval(i) for i in secondPair]):
            sum += 1
    return sum


if __name__ == '__main__':
    f = open('./day4_input.txt', 'r')
    lines = f.readlines()

    print(fullyContainedPairs(lines))
    print(overlappingPairs(lines))
