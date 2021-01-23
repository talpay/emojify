import re

import numpy as np
from nltk import SnowballStemmer, WhitespaceTokenizer
from numpy import dot
from numpy.linalg import norm
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer

import pandas as pd
import json
import spacy
from tqdm import tqdm
import sklearn.metrics

text = """
On a dark desert highway, cool wind in my hair
Warm smell of colitas, rising up through the air
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

pd.DataFrame(emojis, columns=['name', 'unicode', 'keywords'])#.head()

nlp = spacy.load("en_core_web_sm")

with open('./data/glove.6B.300d.txt', 'r') as f:
    for line in tqdm(f, total=400000):
        parts = line.split()
        word = parts[0]
        vec = np.array([float(v) for v in parts[1:]], dtype='f')
        nlp.vocab.set_vector(word, vec)

docs = [nlp(str(keywords)) for _, _, keywords in tqdm(emojis)]
doc_vectors = np.array([doc.vector for doc in docs])


def most_similar(vectors, vec):
    dst = np.dot(vectors, vec) / (norm(vectors) * norm(vec) + 1e-7)
    return np.argsort(-dst), np.sort(-dst)


def emojify(s, most_n=1, threshold=0.02, debug=False):
    v = nlp(str.join('',s)).vector

    ids, dst = most_similar(doc_vectors, v)
    ids = ids[:most_n]
    dst = dst[:most_n] * -1
    html = []
    for name, unicode, keywords in emojis[ids]:
        values = unicode.split(' ')
        for v in values:
            c = chr(int(v.replace('U+', ''), 16))
            html.append(c)
    dstr = ' (' + str(dst) + ', '+ str(ids) + ')' if debug else ''
    if dst < threshold:
        print(s + ' {}'.format(' '.join([x for x in html])) + dstr, end=" ")
    else:
        print(s + dstr, end=" ")

def w_tokenizer(text):
    tokenizer = WhitespaceTokenizer()
    # Use tokenize method
    tokenized_list = tokenizer.tokenize(text)
    return (tokenized_list)

def stemmer_snowball(text_list):
    snowball = SnowballStemmer(language='english')
    return_list = []
    for i in range(len(text_list)):
        return_list.append(snowball.stem(text_list[i]))
    return(return_list)

def preprocessor_final(text):
    if isinstance((text), (str)):
        text = re.sub('<[^>]*>', '', text)
        text = re.sub('[\W]+', '', text.lower())
        return text
    if isinstance((text), (list)):
        return_list = []
        for i in range(len(text)):
            temp_text = re.sub('<[^>]*>', '', text[i])
            temp_text = re.sub('[\W]+', '', temp_text.lower())
            return_list.append(temp_text)
        return(return_list)
    else:
        pass

def pipelinize(function, active=True):
    def list_comprehend_a_function(list_or_series, active=True):
        if active:
            return [function(i) for i in list_or_series]
        else: # if it's not active, just pass it right back
            return list_or_series
    return FunctionTransformer(list_comprehend_a_function, validate=False, kw_args={'active':active})


estimators = [
                ('tokenizer', pipelinize(w_tokenizer)),
                # ('stemmer', pipelinize(stemmer_snowball)),
                ('preprocessor', pipelinize(preprocessor_final))
              ]

pipe = Pipeline(estimators)

sents = pipe.transform([text])

import itertools
words = list(itertools.chain(*sents)) # remove sentence structure

print("\n#######")
threshold = 1
for w in words:
    emojify(w, 1, threshold, debug=False)

print("\n#######")
threshold = 0.02
for w in words:
    emojify(w, 1, threshold, debug=False)