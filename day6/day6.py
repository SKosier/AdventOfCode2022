def removeKey(d, elem):
    if d[elem] == 1:
        d.pop(elem, None)
    else:
        d[elem] = d[elem] - 1


def addKey(d, elem):
    if elem in d:
        d[elem] = d[elem] + 1
    else:
        d[elem] = 1


def calculateMarker(line, limit):
    d = {}
    for elem in line[:limit]:
        addKey(d, elem)
    if len(d) == limit:
        return limit

    head = 0
    marker = limit
    for c in line[limit:]:
        removeKey(d, line[head])
        addKey(d, c)
        head += 1
        marker += 1
        if len(d) == limit:
            return marker


if __name__ == '__main__':
    f = open('./day6_input.txt', 'r')
    line = f.readline()

    print(calculateMarker(line, 4))
    print(calculateMarker(line, 14))
