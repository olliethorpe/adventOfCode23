from utils import cache_and_read_input
import re


def find_sum_of_scratchcard_scores(scratch_cards):
    sum = 0
    for scratch_card in scratch_cards:
        score = 0

        matches = re.search(r":([\d\s]+)\|([\d\s]+)", scratch_card)
        winning_nos = matches.group(1).split()
        given_nos = matches.group(2).split()

        is_first_win = True
        for no in winning_nos:
            if no in given_nos:
                if is_first_win:
                    score = 1
                    is_first_win = False
                else:
                    score = score * 2

        sum += score

    print(sum)


def return_no_wins(scratch_card):
    matches = re.search(r":([\d\s]+)\|([\d\s]+)", scratch_card)
    winning_nos = matches.group(1).split()
    given_nos = matches.group(2).split()

    return sum([1 for no in winning_nos if no in given_nos])


def get_total_no_cards(scratch_cards):
    card_count = {card_no: 1 for card_no, _ in enumerate(scratch_cards)}
    
    for card_no, scratch_card in enumerate(scratch_cards):
        no_wins = return_no_wins(scratch_card)
        for i in range(1, no_wins+1):
            if card_no + i <= len(scratch_cards) - 1:
                card_count[card_no + i] += (1 * card_count[card_no])  # The next card will be added one time per win. If we have 3 lots of the same card then we will add 3

    final_count = sum(card_count.values())

    print(final_count)





scratch_cards = cache_and_read_input(4).split('\n')[:-1]

get_total_no_cards(scratch_cards)