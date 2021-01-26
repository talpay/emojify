import re

import numpy as np

from numpy import dot
from numpy.linalg import norm
import string

import pandas as pd
import json
import spacy
from spacy.matcher import Matcher

from tqdm import tqdm
import sklearn.metrics


import preprocessing as pp

text = """
On a dark desert highway, cool wind in my hair
"Warm smell of colitas, rising up through the air"
Up ahead in the distance, I saw a shimmering light
My head grew heavy and my sight grew dim
I had to stop for the night
There she stood in the doorway;
I heard the mission bell
And I was thinking to myself,
"This could be Heaven or this could be Hell"
Then she lit up a candle and she showed me the way
There were voices down the corridor,
I thought I heard them say...
Welcome to the hotel California
"""

# labels: https://www.kaggle.com/rtatman/emojinet
def load_emojis():
    rows = []
    with open('./data/emojis.json') as f:
        for emoji in json.loads(f.read()):
            rows.append([emoji['name'], emoji['unicode'], ' '.join(emoji['keywords'])])
    return np.array(rows)

emojis = load_emojis()

pd.DataFrame(emojis, columns=['name', 'unicode', 'keywords'])

nlp = spacy.load("en_core_web_sm")

with open('./data/glove.6B.100d.txt', 'r') as f:
    for line in tqdm(f, total=402389):
        parts = line.split()
        word = parts[0]
        vec = np.array([float(v) for v in parts[1:]], dtype='f')
        nlp.vocab.set_vector(word, vec)

docs = [nlp(str(keywords)) for _, _, keywords in tqdm(emojis)]
doc_vectors = np.array([doc.vector for doc in docs])


def most_similar(vectors, vec):
    dst = np.dot(vectors, vec) / (norm(vectors) * norm(vec) + 1e-7)
    return np.argsort(-dst), np.sort(-dst)


def emojify(word, most_n=1):
    v = nlp(str.join('', word)).vector

    ids, dst = most_similar(doc_vectors, v)
    ids = ids[:most_n]
    dst = dst[:most_n] * -1
    e_res = []
    for name, unicode, keywords in emojis[ids]:
        values = unicode.split(' ')
        for v in values:
            c = chr(int(v.replace('U+', ''), 16))
            e_res.append(c)

    #TODO random choice and most_n>1?

    return dst, e_res, ids

def eprint(word, e_res, threshold = 0.02, debug = False):
    dstr = ' (' + str(dst) + ', ' + str(ids) + ')' if debug else ''
    emoji = ' '.join([x for x in e_res])
    if dst < threshold:
        print(word + ' {}'.format(emoji) + dstr, end=" ")
    else:
        print(word + dstr, end=" ")

orig, words = pp.preprocess(text)
o2w = dict(zip(orig, words))

w2e = dict()
for word in words:
    if word not in w2e.keys():
        dst, e_res, ids = emojify(word, 1)
    w2e[word] = e_res

replace = False # word -> emoji vs. word -> word + emoji
# process original text, retain formatting
doc = nlp(text)
newline = True
for oword in doc:
    oword = oword.text

    pre = '' if replace else oword + " "
    #'\n ',
    if oword in string.punctuation :
        # print(" "*(not newline), end="")
        print(oword, end="")#*(not newline))
        # if newline and punct: dont " "
        nowhiteafter = ['"', "'"]
        if oword in nowhiteafter:
            newline = True
        else:
            newline = False
        continue
    if oword in string.whitespace:
        print(oword, end="")
        newline = True
        continue

    print(" "*(not newline) + pre + " ".join(w2e[o2w[oword]]), end="")
    newline = False

# print("####################")
#
# for oword in orig:
#     if oword not in string.punctuation:
#         pre = oword if not replace else ''
#
#         transl = text.replace(oword, pre + ' '.join(w2e[o2w[oword]]))
# print(transl)
#print("\n")

# print("\n#######")
# threshold = 0.02
# for w in words:
#     emojify(w, 1, threshold, debug=False)