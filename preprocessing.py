import re
import itertools
from nltk import SnowballStemmer, WhitespaceTokenizer, BlanklineTokenizer, WordPunctTokenizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from nltk.tokenize import sent_tokenize

import nltk
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

def w_tokenizer(text):
    tokenizer = WhitespaceTokenizer()
    tokenized_list = tokenizer.tokenize(text)
    return (tokenized_list)

def wp_tokenizer(text):
    tokenizer = WordPunctTokenizer()
    tokenized_list = tokenizer.tokenize(text)
    return (tokenized_list)

def s_tokenizer(text):
    return sent_tokenize(text)

def ps_tokenizer(text):
    return sent_detector.tokenize(text.strip())
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

# def pipelinize(function, active=True):
#     def list_comprehend_a_function(list_or_series, active=True):
#         if active:
#             return [function(i) for i in list_or_series]
#         else: # if it's not active, just pass it right back
#             return list_or_series
#     return FunctionTransformer(list_comprehend_a_function, validate=False, kw_args={'active':active})
#
#
#
def preprocess(text):
    # estimators = [
    #                 ('tokenizer', pipelinize(w_tokenizer)),
    #                 # ('stemmer', pipelinize(stemmer_snowball)),
    #                 ('preprocessor', pipelinize(preprocessor_final))
    #               ]
    #
    # pipe = Pipeline(estimators)
    #
    # sents = pipe.transform([text])

    orig = wp_tokenizer(text)
    words = preprocessor_final(orig)

    # orig: unprocessed words
    # words: preprocessed words

    return orig, words

