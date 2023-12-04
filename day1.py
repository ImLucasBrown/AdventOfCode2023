import re


def load_data(filename):
    with open(f'./data/day1/{filename}', 'r') as f:
        data = f.read().splitlines()
    return data


def get_numbers_to_sum(digit_list):
    numbers_to_sum = []
    for item in digit_list:
        d1 = item[0]
        d2 = item[-1]
        number = int(f'{d1}{d2}')
        numbers_to_sum.append(number)
    return numbers_to_sum


def part1(datafile='data.txt'):
    data = load_data(datafile)
    digit_list = []
    for string in data:
        digits = re.findall(r"\d", string)
        if digits:
            digit_list.append(digits)

    numbers_to_sum = get_numbers_to_sum(digit_list)
    answer = sum(numbers_to_sum)
    # print(answer)
    return answer


def part2(datafile='data.txt'):
    data = load_data(datafile)
    valid_words = ['one', 'two', 'three', 'four', 'five',
                   'six', 'seven', 'eight', 'nine']
    pattern = r'(?=(%s))' % '|'.join(valid_words)

    digit_list = []
    line_list = []

    for line in data:
        # Using regex, find any valid words in the line
        # using the valid_words list
        spelled_digits = [m.group(1) for m in re.finditer(pattern, line)]
        _digits = re.findall(r'\d', line)
        # print(spelled_digits)
        for spelled in spelled_digits:
            # Replace the spelled digit with the corresponding digit
            line = line.replace(spelled,
                                str(valid_words.index(spelled) + 1) + spelled)
        # Extract digits
        digits = re.findall(r'\d', line)
        if digits:
            digit_list.append(list(digits))
            line_list.append(line)

    numbers_to_sum = get_numbers_to_sum(digit_list)
    answer = sum(numbers_to_sum)
    # print(answer)
    return answer


def test():
    assert part1('example1.txt') == 142
    print('Part 1 tests passed')
    assert part2('example2.txt') == 281
    print('Part 2 tests passed')


test()
answer1 = part1()
print(f'Answer 1: {answer1}')
answer2 = part2()
print(f'Answer 2: {answer2}')

