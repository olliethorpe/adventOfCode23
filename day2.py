from utils import cache_and_read_input
import re


def get_part_1_answer():
    starting_cubes = {"red": 12, "blue": 14, "green": 13}

    games = cache_and_read_input(2).split('\n')[:-1]

    sum_of_games = 0
    for game in games:
        # print(game)

        impossible_game = False
        game_no = re.findall("Game (\d+)", game)[0]

        # print(game_no)

        cube_reveals = game.split(';')
        for cube_reveal in cube_reveals:
            cubes_revealed = re.findall(r"\d+ (?:red|green|blue)", cube_reveal)

            for cubes in cubes_revealed:
                colour = re.findall(r"red|green|blue", cubes)[0]
                num = re.findall(r"\d+", cubes)[0]

                if int(starting_cubes[colour]) < int(num):
                    impossible_game = True
                    # print(f"impossible game found for game {game_no}, {num} {colour}s is greater than {starting_cubes[colour]}")
                    break

                if cube_reveal == cube_reveals[-1] and cubes == cubes_revealed[-1]:
                    # print(f"game {game_no} has passed the test as we made it to {cubes_revealed[-1]}")
                    sum_of_games += int(game_no)

            if impossible_game:
                break

    print(sum_of_games)


def get_part_2_answer():
    games = cache_and_read_input(2).split('\n')[:-1]

    sum_of_powers = 0
    for game in games:
        starting_cubes = {"red": 0, "blue": 0, "green": 0}

        cube_reveals = game.split(';')
        for cube_reveal in cube_reveals:
            cubes_revealed = re.findall(r"\d+ (?:red|green|blue)", cube_reveal)

            for cubes in cubes_revealed:
                colour = re.findall(r"red|green|blue", cubes)[0]
                num = re.findall(r"\d+", cubes)[0]

                if int(starting_cubes[colour]) < int(num):
                    starting_cubes[colour] = int(num)
        power = 1

        for v in starting_cubes.values():
            power *= v

        sum_of_powers += power

    print(sum_of_powers)
