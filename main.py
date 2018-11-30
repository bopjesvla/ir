import re
import numpy as np
queries = open('queries.txt').read().split('\n')
queries = [q for q in queries if q != '']
from nltk.corpus import stopwords

## wv

from gensim.models import KeyedVectors
vectors = open('VECTORS').read().strip()
x = KeyedVectors.load_word2vec_format(vectors)
stop = set(stopwords.words('english'))

sim = .9

## loop
for sim in range(85, 101):

    ## XML
    i = 0

    def word_synonyms(word):
        if word in stop or word.isdigit():
            return []
        tuples = x.similar_by_word(word, topn=5)
        if any(syn == 's' for syn, _ in tuples):
            print(word)
        return [syn for syn, similarity in tuples if similarity >= sim/100 and syn not in stop]

    def query_synonyms(match):
        text = match.group(0).strip()
        # if text.startswith("description"):
        #     text = text[len("description:"):]
        words = re.findall('\w+', text.lower(), re.UNICODE)

        syns = [s for w in words for s in word_synonyms(w)]

        return '\n' + text + ' ' + ' '.join(syns) + '\n\n'

    txt = open('Anserini/src/main/resources/topics-and-qrels/topics.robust04.301-450.601-700.txt').read()

    descriptions = re.sub(r'(?<=<title>)[\s\S]*?(?=<desc>)', query_synonyms, txt)

    print(sim)

    ## write desc

    with open('query-synonyms-sim-{}.txt'.format(sim), 'w') as f:
        f.write(descriptions)

