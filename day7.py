from utils import cache_and_read_input


r = cache_and_read_input(7)


def find_hand(hand: str):
    d = {}
    for card in hand:
        d[card] = d.get(card, 0) + 1
    return d


hands = r.split('\n')

for hand in hands[:1]:
    hand, bet = hand.split()
    hand = find_hand(hand)
    
