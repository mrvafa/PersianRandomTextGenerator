import argparse
import sys

import requests
from bs4 import BeautifulSoup
from random import shuffle
import codecs
import re

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', help='text length', default=20)

args = parser.parse_args()
LIMIT = int(args.length)

MAIN_URL = 'https://www.digiato.com'
res = requests.get(MAIN_URL)

soup = BeautifulSoup(res.text, 'html.parser')
paragraphs = soup.find_all('p')

text = ''
filename = 'result.txt'

counter = 0
for paragraph in paragraphs:
    if counter < LIMIT:
        try:
            text = text + ' ' + paragraph.text
        except:
            pass

# shuffle list
text = text.split(' ')
## add paragraphs
for _ in range(LIMIT//3):
    text.append('\n')
shuffle(text)

# write list in file
try:
    file = codecs.open(filename, 'w', 'UTF-8')
except Exception as e:
    print(str(e))
    sys.exit()

new_line_counter = 0

text = " ".join(text)

try: 
    file.write(text)
except Exception as e:
    print(str(e))
    sys.exit()

print('Persian Random Text Generated Successfully!\nSee The %s file' % filename)
