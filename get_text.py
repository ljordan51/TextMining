""" This program gets text from a webpage @ project gutenberg and then uses pickle
    to store that text in a file which is then used to copy and paste a selected
    excerpt into koran.txt. This text file is used in mine_text2.py.

    Author : Lakhvinder Jordan <ljordan51@gmail.com>
    Course : Olin Software Design Spring 2017
    Date   : 2017-02-28
"""

import pickle
import requests

# get koran text form project gutenberg
koran = requests.get(
    'http://www.gutenberg.org/cache/epub/2800/pg2800.txt').text

'''
create and open new writable file to dump koran text into
this pickle file is used to create koran.txt by copying and pasting
an excerpt manually
'''
f = open('koran.pickle', 'wb')
pickle.dump(koran, f)
f.close()
