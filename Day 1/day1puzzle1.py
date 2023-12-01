def ParseText(inputString):
    if inputString.isdigit():
        return int(inputString)
    elif inputString == 'zero':
        return 0
    elif inputString == 'one':
        return 1
    elif inputString == 'two':
        return 2
    elif inputString == 'three':
        return 3
    elif inputString == 'four':
        return 4
    elif inputString == 'five':
        return 5
    elif inputString == 'six':
        return 6
    elif inputString == 'seven':
        return 7
    elif inputString == 'eight':
        return 8
    elif inputString == 'nine':
        return 9

def ParseNumberString(inputString):
    output = 0
    toSearch = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    dict = {}
    for i in toSearch:
        count = inputString.count(i)
        if count < 1:
            continue
        lastIndex = 0
        j = 0
        while j < count:
            index = inputString.find(i, lastIndex)
            if (index != -1):
                dict[index] = i
            lastIndex = index + 1
            j += 1
    keys = list(dict.keys())
    keys.sort()
    if len(keys) == 1:
        output += ParseText(dict[keys[0]]) * 10 + ParseText(dict[keys[0]])
    elif len(keys) == 2:
        output += ParseText(dict[keys[0]]) * 10 + ParseText(dict[keys[1]])
    elif len(keys) > 2:
        output += ParseText(dict[keys[0]]) * 10 + ParseText(dict[keys[len(keys) - 1]])

    return output

f = open("C:\\Users\\User\\PycharmProjects\\AoC\\venv\\Inputs\\day1puzzle1.txt")
#f = open("C:\\Users\\User\\PycharmProjects\\AoC\\venv\\Inputs\\day1puzzle1sample.txt")
#f = open("C:\\Users\\User\\PycharmProjects\\AoC\\venv\\Inputs\\day1puzzle1sample2.txt")
sum = 0

for x in f:
    sum += ParseNumberString(x)

f.close()
print(sum)