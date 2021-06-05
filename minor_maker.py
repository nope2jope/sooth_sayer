import requests
import re
from bs4 import BeautifulSoup
from pprint import pprint

response = requests.get(url='https://www.tarotcardmeanings.net/waite-tarot-comments/waite-on-tarot-wands.htm')
response.raise_for_status()
source = response.text

document = BeautifulSoup(source, 'html.parser')

a=(document.find('h2').prettify())


b = document.find('h2')

c = b.next_element

d = c.next_element

e= d.next_element

f = e.next_element

g = f.next_element

h = g.next_element

i = h.next_element

j = i.next_element

k = j.next_element

l = k.next_element

m = l.next_element

n = m.next_element

o = n.next_element

p = o.next_element

# up meaning got right
head = n
meaning = p
up_mean = head + meaning

q = p.next_element

r = q.next_element

s = r.next_element

t = s.next_element

u = t.next_element

v = u.next_element

# reversed meaning got right
rev = v
rev_mean = v + v.next_element

print(up_mean)
print(rev_mean)






def fetch_minor_arcana(doc):
    h2s = doc.find_all('h2')
    count = 0
    titles = []

    for h in h2s:
        if count < 14:
            if 'name':
                face = h.text
                titles.append(face)
                count += 1

    return titles

