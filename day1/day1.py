def countCalories(lines):
    sum = 0
    calories = []
    for l in lines:
        if l.strip() == "":
            calories.append(sum)
            sum = 0
        else:
            sum += int(l)
    return sorted(calories)

if __name__ == '__main__':
    f = open('./day1_input.txt', 'r')
    lines = f.readlines()

    print(max(countCalories(lines)))
    print(sum((countCalories(lines))[-3:]))

    f.close()
