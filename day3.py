from utils import cache_and_read_input


def calculate_part_1_answer(engine_schematic):
    sum_of_part_nos = 0
    for line_no, line in enumerate(engine_schematic):
        # I am not proud of this code
        line = engine_schematic[line_no]
        line = engine_schematic[line_no] = line + '.'

        part_no = ''

        for digit_no in range(len(line)):
            digit = line[digit_no]
            try:
                int(digit)
                part_no += digit

            except ValueError as _:
                if part_no:
                    # print(f"possible part number found: {part_no}")
                    possibly_part_number = []

                    # get symbol left and right of part_no
                    left_of_part_no = line[digit_no - (len(part_no) + 1)]
                    right_of_part_no = line[digit_no]
                    # print(f"Left of part number is {left_of_part_no}")
                    # print(f"Right of part number is {right_of_part_no}")

                    # Check symbols above/below
                    lines_above_below = [line_no - 1, line_no + 1]

                    for above_below in lines_above_below:
                        if above_below >= 0 and above_below <= len(engine_schematic)-1:
                            # print(f"Checking line {above_below}")

                            for symbol_index in range(len(part_no)+2):
                                if digit_no - symbol_index >= 0 and digit_no - symbol_index <= len(engine_schematic[above_below])-1:
                                    symbol_above_below = engine_schematic[above_below][digit_no - symbol_index]
                                    possibly_part_number.append(symbol_above_below != '.' and not symbol_above_below.isdigit())
                                    # print(f"symbol at index {digit_no - symbol_index} is {symbol_above_below}, this evaluates to {symbol_above_below != '.' and not symbol_above_below.isdigit()}")


                    possibly_part_number.extend([symbol != '.' for symbol in [left_of_part_no, right_of_part_no]])
                    is_part_number = any(possibly_part_number)
                    if is_part_number:
                        sum_of_part_nos += int(part_no)

                    # print(f"Is part no: {is_part_number}")
                part_no = ''
    print(sum_of_part_nos)

if __name__ == "__main__":
    engine_schematic = cache_and_read_input(3).split('\n')[:-1]

    sum_of_gear_products = 0

    # Find a *
    for line_no, line in enumerate(engine_schematic):
        for symbol_no, symbol in enumerate(line):
            if symbol == '*':

                # Search around it for numbers

                # left
                if symbol_no > 0 and line[symbol_no - 1].isdigit():
                    # find the entire number
                    pass
                # right
                if symbol_no != len(line) -1 and line[symbol_no - 1].isdigit():
                    # find the entire number
                    pass
                # above




    # If there are EXACTLY 2 adjacent part numbers, find the numbers in their entirety

    # Find product of them 
