import random

# determines positional of the card
def flip_card():
    pos = [0,1]
    position = random.choice(pos)

    if position == 0:
        return 'Upright'
    elif position == 1:
        return 'Reversed'

# selects and compiles cards given a chosen spread, deck
def fortune_teller(deck, spread):
    reading = []

    for _ in range(spread):
        card = random.choice(deck)
        position = flip_card()
        fortune = {
            'name': card['name'],
            'img_url': card['img_url'],
            'meaning': card['meaning'][position],
        }

        reading.append(fortune)

    return reading

