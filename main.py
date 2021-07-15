from major_maker import MajorMaker
from minor_maker import MinorMaker
from croupier import fortune_teller

major_arcana = MajorMaker().major_cards
minor_arcana = MinorMaker().minor_cards

tarot_deck = major_arcana + minor_arcana

spread = [1, 3, 4, 10]

fortune = fortune_teller(deck=tarot_deck, spread=3)

for card in fortune:
    print(card['img_url'])
    print(card['name'])
    print(card['meaning'] + '\n')


