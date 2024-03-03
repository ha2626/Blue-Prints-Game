file_path = 'buildings.txt'
with open(file_path, 'r') as file:
    contents = file.read()

# print(contents)
# Remove the initial and trailing triple quotes
data_str = contents.strip()[3:-3]

# Split the string by triple quotes to get each row
rows = contents.split('```')

# Remove any empty strings resulting from splitting
rows = [row.strip() for row in rows if row.strip()]

# Split each row by newline to get the individual elements
list_of_lists = [row.split('\n') for row in rows]
# print(list_of_lists[2])

def recycled_green(list_of_lists):
    count = 0
    score = 0
    for list in list_of_lists:
        for item in list:
            if "R" in item:
                count += 1
    # print(count)
    if count == 1:
        score = 2
    elif count == 2:
        score = 5
    elif count == 3:
        score = 10
    elif count == 4:
        score = 15
    elif count == 5:
        score = 20
    elif count == 6:
        score = 30
    return score

def glass_clear(list_of_lists):
    my_list = list_of_lists
    # for list in list_of_lists[0]:
    strings = [item.replace('-', '').replace('|', '') for item in my_list]
    # print(strings)
    myarr = []
    for x in strings:
        if 'G' in x:
            # print(x)
            num = ""
            # myarr = []
            collect_number = False
            for character in x:
                if character == 'G':
                    collect_number = True
                elif character.isalpha() and character != 'G':
                    if len(num) > 0:
                        myarr.append(int(num))
                        num = ""
                    collect_number = False
                if collect_number:
                    if character.isdigit():
                        # print(character)
                        num += character
                    else:
                        if len(num) > 0:
                            myarr.append(int(num))
                        num = ""
                #
            if len(num) > 0:
                myarr.append(int(num))

    return (sum(myarr))


def fibonacci_score(level):
    if level < 0:
        return 0
    match level:
        case 0:
            return 1
        case 1:
            return 2
        case _:
            if level <= 4:
                return fibonacci_score(level - 1) + fibonacci_score(level - 2)  # Recursive case
            else:
                return 8

def stone_black(list_of_lists):
    my_list = list_of_lists
    # for list in list_of_lists[0]:
    strings = [item.replace('-','').replace('|','') for item in my_list]
    count = 1
    sum = 0
    for x in reversed(strings):
        if 'S' in x:
            # print(f'S exists in level: {count}')
            sum = sum + fibonacci_score(count)
        count = count + 1
    return sum

def orange_wood(list_of_lists):
    my_list = list_of_lists
    matrix = [row.split('|') for row in my_list]
    # print(matrix)
    score = 0
    row_count = 0
    for item in matrix:
        # print(item)
        for x in range(0,len(item)):
            if 'W' in item[x]:
                # print(f'Looking at item:{item[x]}')
                if (item[x + 1]) != '--':
                    score += 2
                if x != 0 and (item[x - 1]) != '--':
                    # print(x)
                    # print(item[x - 1]) This was returning the last element in the matrix when x was 0, so
                    score += 2
                if ((row_count - 1) >= 0) and ((matrix[row_count - 1][x]) != '--'):
                    # print(row_count)
                    # print(x)
                    # print(matrix[row_count - 1][x])
                    score += 2
                if ((row_count + 1) < len(matrix)) and ((matrix [row_count+1][x]) != '--'):
                    # print(matrix[row_count+1][x])
                    score += 2
        row_count = row_count + 1
        print(score)
    return score

def print_output_to_file(data, file):
    total = sum(quantity for _, quantity in data)
    max_length = max(len(item[0]) for item in data)  # Find the maximum length of items

    # Write the header to the file
    file.write("+{}+----+\n".format('-' * (max_length + 2)))

    # Write the data to the file
    for item in data:
        file.write("| {:<{}} | {:>2} |\n".format(item[0], max_length, item[1]))

    # Write the total to the file
    file.write("+{}+====+\n".format('=' * (max_length + 2)))
    file.write("| {:<{}} | {:>2} |\n".format('total', max_length, total))
    file.write("+{}+----+\n".format('-' * (max_length + 2)))


def main():
    with open('scoring-results.txt', 'w') as output_file:
        output_file.write("```\n")
        choice = len(list_of_lists)
        for choice in range(choice):
                for item in list_of_lists[choice]:
                    output_file.write(item + '\n')
                output_file.write('\n')

                A = glass_clear(list_of_lists[choice])
                B = recycled_green(list_of_lists[choice])
                C = stone_black(list_of_lists[choice])
                D = orange_wood(list_of_lists[choice])

                data = [
                    ("glass", A),
                    ("recycled", B),
                    ("stone", C),
                    ("wood", D),
                ]
                print_output_to_file(data, output_file)
                output_file.write("```\n")


main()

orange_wood(list_of_lists[3])