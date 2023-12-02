def checkMatch(entry):
    red = 0
    green = 0
    blue = 0

    entryList = entry.split(', ')
    for subentry in entryList:
        splitSubentry = subentry.split(' ')
        if splitSubentry[1] == 'red':
            red += int(splitSubentry[0])
        elif splitSubentry[1] == 'green':
            green += int(splitSubentry[0])
        elif splitSubentry[1] == 'blue':
            blue += int(splitSubentry[0])

    if red <= 12 and green <= 13 and blue <= 14:
        return True

    return False

def checkEntries(filename):
    f = open(filename)
    total = 0

    for line in f:
        startList = line.split(': ')
        gameId = int(startList[0].replace('Game ', ''))
        colours = startList[1].strip().split('; ')
        correct = 0
        for elem in colours:
            if checkMatch(elem) == False:
                break
            else:
                correct += 1
            if correct == len(colours):
                total += gameId

    return total

#print(checkEntries('day2sample'))
print(checkEntries('day2input'))