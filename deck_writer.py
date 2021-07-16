from major_maker import MajorMaker
from minor_maker import MinorMaker
from pprint import pprint
import csv
import pandas


class CardManager:

    # this function should only be run in the absence of an extant csv file
    # saves time scraping, bot flagging, makes information static
    def write_deck(self):
        major_arcana = MajorMaker().major_cards
        minor_arcana = MinorMaker().minor_cards

        deck = major_arcana + minor_arcana

        with open('tarot_deck.csv', 'a', newline='') as file:
            fields = ['name', 'img_url', 'meaning_upright', 'meaning_reversed']
            writer = csv.DictWriter(file, fieldnames=fields)

            writer.writeheader()
            for card in deck:
                writer.writerow({'name': card['name'], 'img_url': card['img_url'],
                                 'meaning_upright': card['meaning']['Upright'],
                                 'meaning_reversed': card['meaning']['Reversed']})

    def fetch_deck(self):
        df = pandas.read_csv('tarot_deck.csv')
        # translates df to iterrable dictionary
        dictionary = df.to_dict('index')

        d = []

        # reformats entries into recognizable template
        # with the addition of an id inherited from csv/dataframe
        for i in dictionary:
            card = {
                'id': i,
                'name': dictionary[i]['name'],
                'img_url': dictionary[i]['img_url'],
                'meaning': {'Upright': dictionary[i]['meaning_upright'],
                            'Reversed': dictionary[i]['meaning_reversed']},
            }
            d.append(card)

        return d
