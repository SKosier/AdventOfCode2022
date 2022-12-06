shapePoints = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3
}

winOrLosePoints = {
    -1: 0,
    0: 3,
    1: 6
}

result = {
    "X": -1,
    "Y": 0,
    "Z": 1,
}


def gameRound(played):
    if shapePoints[played[0]] == shapePoints[played[1]]:
        return 0
    if shapePoints[played[0]] - shapePoints[played[1]] == -1:
        return 1
    if shapePoints[played[0]] - shapePoints[played[1]] == 2:
        return 1
    else:
        return -1


def figurePointsOfMustPlayedShape(column):
    if result[column[1]] == 0:
        return shapePoints[column[0]]
    if result[column[1]] == 1:
        return (shapePoints[column[0]] % 3) + 1
    else:
        points = shapePoints[column[0]] - 1
        if points == 0:
            return 3
        return points

def scoreStrategy1(lines):
    score = 0
    for l in lines:
        played = l.strip().split(' ')
        score += winOrLosePoints[gameRound(played)] + shapePoints[played[1]]
    return score

def scoreStrategy2(lines):
    score = 0
    for l in lines:
        columns = l.strip().split(' ')
        score += winOrLosePoints[result[columns[1]]] + figurePointsOfMustPlayedShape(columns)
    return score

if __name__ == '__main__':
    f = open('./day2_input.txt', 'r')
    lines = f.readlines()
    print(scoreStrategy1(lines))
    print(scoreStrategy2(lines))
    f.close()
