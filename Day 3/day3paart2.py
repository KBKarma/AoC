def load_list(filename):
    file_list = []
    f = open(filename)

    for line in f:
        print(line)
        line_list = []
        for char in line.strip():
            line_list.append(char)
        file_list.append(line_list)

    f.close()
    return file_list


def symbol_hunt(row_index, column_index, length_of_int, list_to_search):
    row_index_start = row_index - 1
    if row_index_start < 0:
        row_index_start = row_index

    row_index_end = row_index + 1
    if row_index_end > len(list_to_search) - 1:
        row_index_end = row_index

    column_index_start = column_index - 1
    if column_index_start < 0:
        column_index_start = column_index

    column_index_end = column_index + length_of_int
    if column_index_end > len(list_to_search) - 1:
        column_index_end = column_index + length_of_int

    for i in range(row_index_start, row_index_end + 1):
        for j in range(column_index_start, column_index_end + 1):
            test = list_to_search[i][j]
            if list_to_search[i][j].isdigit() is False and list_to_search[i][j] != '.':
                return True

    return False


def find_adjacencies(list_to_use):
    running_total = 0

    for i in range(len(list_to_use)):
        number = 0
        for j in range(len(list_to_use[i])):
            i_len = len(list_to_use)
            j_len = len(list_to_use[i])
            current_char = list_to_use[i][j]
            if list_to_use[i][j].isdigit() and number == 0:
                number += int(list_to_use[i][j])
            elif list_to_use[i][j].isdigit() and number != 0:
                number *= 10
                number += int(list_to_use[i][j])
                if j == len(list_to_use[i]) - 1:
                    number_len = len(str(number))
                    result = symbol_hunt(i, j - number_len, number_len, list_to_use)
                    if result:
                        running_total += number
                    number = 0
            elif list_to_use[i][j].isdigit() is False and number != 0:
                number_len = len(str(number))
                result = symbol_hunt(i, j - number_len, number_len, list_to_use)
                if result:
                    running_total += number
                number = 0

    return running_total


# operand_list = load_list('day3sample1')
operand_list = load_list('day3input')
print(find_adjacencies(operand_list))
