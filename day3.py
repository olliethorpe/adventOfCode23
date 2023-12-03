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



def get_entire_part_no(line, symbol_index):
    part_no = ''

    # find start of number
    while symbol_index >= 0 and line[symbol_index].isdigit():
        symbol_index -= 1
    symbol_index += 1
    # obtain whole number
    while symbol_index <= len(line) - 1 and line[symbol_index].isdigit():
        part_no += line[symbol_index]
        symbol_index += 1
    return part_no

if __name__ == "__main__":
    engine_schematic = cache_and_read_input(3).split('\n')[:-1]

    sum_of_gear_products = 0

    # Find a *
    for line_no, line in enumerate(engine_schematic):
        for symbol_no, symbol in enumerate(line):
            parts = []
            if symbol == '*':

                # Search around it for numbers

                # left
                if symbol_no > 0 and line[symbol_no - 1].isdigit():
                    parts.append(get_entire_part_no(line, symbol_no - 1))  
                # right
                if symbol_no < len(line) - 1 and line[symbol_no + 1].isdigit():
                    # find the entire number
                    parts.append(get_entire_part_no(line, symbol_no + 1))

                parts_above = set()
                parts_below = set()

                for x in range(-1, 2):
                    symbol_above_below_no = symbol_no + x

                    if symbol_above_below_no >= 0 and symbol_above_below_no < len(line):

                        if line_no > 0 and engine_schematic[line_no - 1][symbol_above_below_no].isdigit():
                            line_above = engine_schematic[line_no - 1]
                            part_no_above = get_entire_part_no(line_above, symbol_above_below_no)
                            parts_above.add(part_no_above)
                            # print(f"Adding part to parts list for above the astrix {part_no_above}")

                        if line_no < len(engine_schematic) - 1 and engine_schematic[line_no + 1][symbol_above_below_no].isdigit():
                            line_below = engine_schematic[line_no + 1]
                            part_no_below = get_entire_part_no(line_below, symbol_above_below_no)
                            parts_below.add(part_no_below)
                            # print(f"Adding part to parts list for below the astrix {part_no_below}")

                parts.extend(list(parts_above))
                parts.extend(list(parts_below))

                print(f"Parts found for the astrix in position {symbol_no} on line {line_no}: {parts}")
                if len(parts) == 2:
                    product_of_gears = 1
                    for gear in parts:
                        product_of_gears = product_of_gears * int(gear)

                    sum_of_gear_products += product_of_gears

    print(sum_of_gear_products)
