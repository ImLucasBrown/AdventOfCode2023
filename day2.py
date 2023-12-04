import re


colors = ['red', 'green', 'blue']


def load_data(filename):
    games = []
    with open(f'./data/day2/{filename}', 'r') as f:
        for line in f.readlines():
            game_number, raw_sets = line.split(':')
            game_number = int(game_number.split(' ')[1])
            raw_sets = raw_sets.split(';')
            draws = []
            for draw in raw_sets:
                gems = draw.split(',')
                gem_set = {colors[0]: 0, colors[1]: 0, colors[2]: 0}
                for gem in gems:
                    for color in colors:
                        if color in gem:
                            break
                    gem_count_str = gem.split(color)[0]
                    gem_set[color] = int(gem_count_str)
                draws.append(gem_set)
            game_data = {'game_id': game_number, 'draws': draws}
            games.append(game_data)
    return games


def part1(datafile='data.txt'):
    known_counts = {'red': 12, 'green': 13, 'blue': 14}
    games_played = load_data(datafile)
    possible_games = []
    for game in games_played:
        game_id = game['game_id']
        possible = True
        for draw in game['draws']:
            for color in colors:
                if draw[color] > known_counts[color]:
                    possible = False
                    break
        if possible:
            possible_games.append(game_id)
    answer = sum(possible_games)
    return answer


def part2(datafile='data.txt'):
    known_counts = {'red': 12, 'green': 13, 'blue': 14}
    games_played = load_data(datafile)
    answer = 0
    powers = []
    for game in games_played:
        game_id = game['game_id']
        max_counts = {colors[0]: 0, colors[1]: 0, colors[2]: 0}
        for draw in game['draws']:
            for color in colors:
                max_counts[color] = max(max_counts[color], draw[color])
        max_values = list(max_counts.values())
        power = -1
        for i, max_val in enumerate(max_values):
            try:
                next_item = max_values[i + 1]
            except IndexError:
                next_item = 1
            if power < 0:
                power = max_val
            power = power * next_item
        powers.append(power)
        answer += power
    return answer


def test():
    assert part1('example.txt') == 8
    assert part2('example.txt') == 2286


test()
answer1 = part1()
print(f'Answer 1: {answer1}')
answer2 = part2()
print(f'Answer 2: {answer2}')


