import pandas as pd
queries = open('queries.txt').read().split('\n')
queries = [q for q in queries if q != '']

## wv

from gensim.models import KeyedVectors
vectors = open('VECTORS').read().strip()
x = KeyedVectors.load_word2vec_format(vectors)

## queries

