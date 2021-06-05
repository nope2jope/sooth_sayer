from major_maker import MajorMaker
from minor_maker import MinorMaker
from pprint import pprint

major_arcana = MajorMaker().major_cards
minor_arcana = MinorMaker().minor_cards

tarot_deck = major_arcana + minor_arcana

pprint(tarot_deck)

