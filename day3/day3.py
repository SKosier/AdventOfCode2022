def calculatePriority(lines):
    sum = 0
    for l in lines:
        l = l.strip()
        first_half = set(l[:len(l) // 2])
        second_half = set(l[len(l) // 2:])
        intersection = first_half.intersection(second_half)
        p = intersection.pop()
        if 'A' <= p <= 'Z':
            sum += ord(p) - 65 + 1 + 26
        if 'a' <= p <= 'z':
            sum += ord (p) - 97 + 1
    return sum

def calculateGroupPriority(lines):
    sum = 0
    for i in range(0, len(lines), 3):
        intersection = set(lines[i].strip()).intersection(set(lines[i+1].strip())).intersection(lines[i+2].strip())
        p = intersection.pop()
        if 'A' <= p <= 'Z':
            sum += ord(p) - 65 + 1 + 26
        if 'a' <= p <= 'z':
            sum += ord (p) - 97 + 1
    return sum

if __name__ == '__main__':
    f = open('./day3_input.txt', 'r')
    lines = f.readlines()

    print(calculatePriority(lines))
    print(calculateGroupPriority(lines))

