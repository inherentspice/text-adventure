# import libraries

from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet, stopwords

# tokenize web-scraping text
text = 'On June 1, 1865, Senator Charles Sumner referred to the most famous speech ever given by President Abraham Lincoln. In his eulogy on the slain president'
tokenized = word_tokenize(text)

# remove stop words
stop_words = set(stopwords.words('english'))
filtered_sentence = []

for t in tokenized:
    if t not in stop_words:
        filtered_sentence.append(t)

print(tokenized)
print(filtered_sentence)

