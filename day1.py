import re
from utils import get_input


def get_part_1_answer(input):
    sum = 0
    for line in input:
        numbs_in_line = re.findall(r"\d", line)
        first_no = numbs_in_line[0]
        last_no = numbs_in_line[-1]

        number_as_str = f"{str(first_no)}{str(last_no)}"

        final_no = int(number_as_str)

        sum += final_no

    return sum


def generate_part_2_answer(input):
    sum = 0
    wordNums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbs = {v: i + 1 for i, v in enumerate(wordNums)}

    for line in input:
        f = []
        for i in range(len(line)):
            for ix in range(i, len(line)+1):
                sub_string = line[i:ix]
                if sub_string in wordNums or (sub_string.isdigit() and len(sub_string) == 1):
                    f.append(sub_string)
                    break

        first_no = numbs[f[0]] if f[0] in numbs.keys() else f[0]
        last_no = numbs[f[-1]] if f[-1] in numbs.keys() else f[-1]

        number_as_str = f"{str(first_no)}{str(last_no)}"
        final_no = int(number_as_str)
        sum += final_no

    return sum


if __name__ == "__main__":
    response = get_input(1)
    r = response.text.split('\n')[:-1]
    print(get_part_1_answer(r))

    print(generate_part_2_answer(r))
