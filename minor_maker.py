import requests
from bs4 import BeautifulSoup


class MinorMaker:
    def __init__(self):
        self.template = {
            'name': '',
            'id': '',
            'img_url': '',
            'meaning': {
                'Upright': '',
                'Reversed': '',
            }
        }

        self.houses = ['wands', 'cups', 'swords', 'pentacles']

        def pull_sources():
            suit_dict_list = []

            for house in self.houses:
                response = requests.get(
                    url=f'https://www.tarotcardmeanings.net/waite-tarot-comments/waite-on-tarot-{house}.htm')
                response.raise_for_status()
                source = response.text
                document = BeautifulSoup(source, 'html.parser')

                suit_dict_list.append({house: document})

            return suit_dict_list

        self.sources = pull_sources()

        def fetch_minor_arcana(doc):

            h2s = doc.find_all('h2')
            count = 0
            labels = []

            for h in h2s:
                if count < 14:
                    if 'name':
                        face = h.text
                        labels.append(face)
                        count += 1

            return labels

        def fetch_minor_meaning(doc):

            minors = []
            h2s = doc.find_all('h2')
            count = 0

            for _ in h2s:
                if count < 14:
                    # ad hoc error handling — this card is formatted differently on source site
                    if _.text == 'Two of Cups':
                        up_mean = str(_.next_element.next_element.next_element.next_element.next_element
                                      .next_element.next_element.next_element.next_element.next_element
                                      .next_element.next_element.next_element.next_element)[1:]
                        rev_mean = str(_.next_element.next_element.next_element.next_element.next_element
                                       .next_element.next_element.next_element.next_element.next_element
                                       .next_element.next_element.next_element.next_element.next_element
                                       .next_element.next_element.next_element.next_element.next_element
                                       .next_element.next_element.next_element.next_element.next_element
                                       .next_element.next_element.next_element.next_element)[1:]
                        template = {
                            'Upright': up_mean,
                            'Reversed': rev_mean,
                        }

                        minors.append(template)
                        count += 1

                    else:
                        up_mean = str(_.next_element.next_element.next_element.next_element.next_element
                                      .next_element.next_element.next_element.next_element.next_element
                                      .next_element.next_element.next_element.next_element)[1:]

                        rev_mean = str(_.next_element.next_element.next_element.next_element.next_element
                                       .next_element.next_element.next_element.next_element.next_element
                                       .next_element.next_element.next_element.next_element.next_element
                                       .next_element.next_element.next_element.next_element.next_element
                                       .next_element)[1:]

                        template = {
                            'Upright': up_mean,
                            'Reversed': rev_mean,
                        }

                        minors.append(template)
                        count += 1

            return minors

        def compile_house(labels, meanings):
            deck = []
            for i in range(14):
                card = {
                    'name': labels[i],
                    'id': i + 1,
                    'img_url': 0,
                    'meanings': meanings[i],
                }
                deck.append(card)
            return deck

        self.minor_cards = []
        count = 0

        # assembles minor cards into self.minor_cards variable
        for house in self.houses:
            l = fetch_minor_arcana(doc=self.sources[count][house])
            m = fetch_minor_meaning(doc=self.sources[count][house])
            d = compile_house(labels=l, meanings=m)
            self.minor_cards.append(d)
            count += 1

        # isolates inner list from outer, redundant listing
        self.minor_cards = self.minor_cards[0]
