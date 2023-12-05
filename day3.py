import re


def load_data(filename):
    with open(f'./data/day3/{filename}', 'r') as f:
        data = f.readlines()
    return data


def contains_symbol(string):
    # Look for anything that isn't a letter, number, or . (dot)
    pattern = re.compile(r'[^\w\s\d.]')
    search = pattern.search(string)
    return bool(search)


def part1(datafile='data.txt'):
    data = load_data(datafile)
    valid_numbers = []
    for i, line in enumerate(data):
        try:
            prev_line = data[max(i - 1, 0)]
            if prev_line == line:
                prev_line = ''
        except IndexError:
            prev_line = ''
        try:
            next_line = data[i + 1]
        except IndexError:
            next_line = ''
        # Find digits in line
        numbers = re.findall(r'\d+', line)
        re.finditer(r'\d+', line)
        # print(numbers)
        # Find index range of digits in line
        ranges = [(m[0], m.start(), m.end()) for m in re.finditer(r'\d+', line)]
        # print(ranges)
        # Check previous line for symbols at digit indices plus/minus 1
        for number, start, end in ranges:
            # Check line before
            if contains_symbol(prev_line[max(start - 1, 0):end + 1]):
                valid_numbers.append(int(number))
                continue
            # Check line after
            elif contains_symbol(next_line[max(start - 1, 0):end + 1]):
                valid_numbers.append(int(number))
                continue
            # Check current line
            elif contains_symbol(line[max(start - 1, 0):end + 1]):
                valid_numbers.append(int(number))
                continue
    answer = sum(valid_numbers)
    return answer


def test():
    assert part1('example.txt') == 4361


test()
answer1 = part1()
print(f'Answer 1: {answer1}')
