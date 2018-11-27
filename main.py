import re
queries = open('queries.txt').read().split('\n')
queries = [q for q in queries if q != '']
from nltk.corpus import stopwords

## wv

from gensim.models import KeyedVectors
vectors = open('VECTORS').read().strip()
x = KeyedVectors.load_word2vec_format(vectors)
stop = set(stopwords.words('english'))

## XML
i = 0

def word_synonyms(word):
    if word in stop or word.isdigit():
        return [word]
    tuples = x.similar_by_word(word, topn=5)
    return [word] + [syn for syn, similarity in tuples if similarity > 0.9 and syn not in stop]

def query_synonyms(match):
    text = match.group(0).strip().lower()
    # if text.startswith("description"):
    #     text = text[len("description:"):]
    global i
    i += 1
    words = re.findall('\w+', text, re.UNICODE)

    words = [s for w in words for s in word_synonyms(w)]

    return '\n' + ' '.join(words) + '\n\n'

txt = open('Anserini/src/main/resources/topics-and-qrels/topics.robust04.301-450.601-700.txt').read()

descriptions = re.sub(r'(?<=<title>)[\s\S]*?(?=<desc>)', query_synonyms, txt)

print(i)

## write desc

with open('query-synonyms.txt', 'w') as f:
    f.write(descriptions)

## queries

