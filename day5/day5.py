import queue

test = [
    "ZN",
    "MCD",
    "P"
]

init = [
    "CZNBMWQV",
    "HZRWCB",
    "FQRJ",
    "ZSWHFNMT",
    "GFWLNQP",
    "LPW",
    "VBDRGCQJ",
    "ZQNBW",
    "HLFCGTJ",
]


def initQueue(letters):
    q = queue.LifoQueue()
    for l in letters:
        q.put(l)
    return q


def extract(l):
    parts = l.split()
    return int(parts[3]), int(parts[5]), int(parts[1])


def task1(lines, bricks):
    for l in lines:
        src, dest, quantity = extract(l)
        for i in range(quantity):
            bricks[dest - 1].put(bricks[src - 1].get())

    return [b.get() for b in bricks]


def task2(lines, bricks):
    for l in lines:
        src, dest, quantity = extract(l)
        if quantity == 1:
            bricks[dest - 1].put(bricks[src - 1].get())
        else:
            helpQ = queue.LifoQueue()
            for i in range(quantity):
                helpQ.put(bricks[src - 1].get())
            for i in range(quantity):
                bricks[dest - 1].put(helpQ.get())

    return [b.get() for b in bricks]


if __name__ == '__main__':
    f = open('./day5_input.txt', 'r')
    lines = f.readlines()

    bricks = [initQueue(i) for i in init]
    print(task1(lines, bricks))
    bricks = [initQueue(i) for i in init]
    print(task2(lines, bricks))
