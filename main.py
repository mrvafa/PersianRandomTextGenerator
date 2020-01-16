import argparse
import sys

import requests
from bs4 import BeautifulSoup
from random import shuffle
import codecs
import re


def get_text(url):
    res = requests.get(url)
    if res.status_code == 200:
        texts = BeautifulSoup(res.text, 'html.parser').find_all('p')
        result = ''
        for text in texts:
            result += re.sub(r'\s+', ' ', text.text)
        return result
    return ''


parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', help='text length', default=20)

args = parser.parse_args()
LIMIT = int(args.length)

MAIN_URL = 'https://www.varzesh3.com'
res = requests.get(MAIN_URL)

soup = BeautifulSoup(res.text, 'html.parser')
posts = soup.find_all('li')

text = ''
filename = 'result.txt'

counter = 0
for post in posts:
    if counter < LIMIT:
        try:
            url = post.find('a')['href']
            if '/news/' in url and 'live' not in url:
                text = text + ' ' + get_text(MAIN_URL + url)
                counter += 1
        except:
            pass

# shuffle list
text = text.split(' ')
shuffle(text)

# write list in file
try:
    file = codecs.open(filename, 'w', 'UTF-8')
except Exception as e:
    print(str(e))
    sys.exit()

new_line_counter = 0

for i in text:
    if new_line_counter < 200:
        file.write(i + ' ')
    else:
        file.write(i + '\n')

print('Persian Random Text Generated Successfully!\nSee The %s file' % filename)
