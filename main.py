import requests
import re
from pprint import pprint
from bs4 import BeautifulSoup

TEMPLATE = {
    'name': '',
    'id': '',
    'img_url': '',
    'meaning': {
        'Upright': '',
        'Reversed': '',
    }
}

response = requests.get(url='https://www.alittlesparkofjoy.com/tarot-cards-list/')
response.raise_for_status()

source = response.text

document = BeautifulSoup(source, 'html.parser')


# splits text elements by first instance of capitals (i.e. "Foo barFoobar" -> ["Foo bar", "Foobar"]
def break_string(string):
    output = filter(None, re.split("([A-Z][^A-Z]*)", string))
    d = [e for e in output]
    return d


# finds card names
def fetch_labels(doc):
    labels = doc.find_all('h4')
    labels_list = []

    for label in labels:
        if "(" in label.text:
            lab = label.text
            labels_list.append(lab)

    return labels_list


# finds card meanings
def fetch_majors(doc):
    majors = doc.find_all(class_='wp-block-table')
    majors_list = []

    for entry in majors:
        m_data = break_string(entry.text)
        majors_list.append(m_data)

    return majors_list


# finds image urls
def fetch_images(doc):
    images = doc.find_all('img')
    images_list = []
    # retrieves ALL instances of the .webp format used for card faces
    for img in images:
        a = (img['src'])
        # only the first twenty-two relevant to the major arcana
        # TODO: ideally would be pared down to just the relevant entries
        if '.webp' in a:
            images_list.append(a)

    return images_list


# reformats information -- depends on step variable instead of length of relevant lists/card ids
# TODO: work on the above to tighten
def compile_majors(labels, majors, images):
    deck = []
    step = 0
    for _ in labels:
        card = {
            'name': l[step],
            'id': step,
            'img_url': images[step],
            'meaning': {
                'Upright': majors[step][1],
                'Reversed': majors[step][3],
            }
        }
        step += 1

        deck.append(card)

    return deck


l = fetch_labels(doc=document)

m = fetch_majors(doc=document)

i = fetch_images(doc=document)

majors_deck = compile_majors(labels=l, majors=m, images=i)

pprint(majors_deck)
