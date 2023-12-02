def find_minimum(entry):
    red = 0
    green = 0
    blue = 0

    entry_list = entry.split('; ')
    for elem in entry_list:
        sub_elem = elem.split(', ')
        for split_elem in sub_elem:
            split_subelem = split_elem.split(' ')
            number = int(split_subelem[0])
            if split_subelem[1] == 'red' and number > red:
                red = number
            elif split_subelem[1] == 'green' and number > green:
                green = number
            elif split_subelem[1] == 'blue' and number > blue:
                blue = number

    return red * green * blue

def check_entries(filename):
    f = open(filename)
    total = 0

    for line in f:
        total += find_minimum(line.split(': ')[1].strip())

    return total

#print(check_entries('day2sample'))
print(check_entries('day2input'))