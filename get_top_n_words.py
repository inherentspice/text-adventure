# import libraries
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv

#preprocess csv
rows = []
with open('five_options_questions.csv', 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        rows.append(row)


#load text that you want to count word frequencies
text = ''
for i in rows:
    for char in i:
        text += char

# function that tokenizes, removes stop words, vectorizers, and counts the most common words
def get_top_n_words(text, n=None):
    """
    List the top n words in a vocabulary according to occurrence in a text without very common words.

    get_top_n_words('fish, flew dangerously far toward the flying fly for only the
    fly near a flying fish is truly a fly, 2')
    -->
    [('fly', 3),
    ('fish', 2)]
    """
    tokenized = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_sentence = []

    for t in tokenized:
        if t not in stop_words:
            filtered_sentence.append(t)
    vec = CountVectorizer().fit(filtered_sentence)
    bag_of_words = vec.transform(filtered_sentence)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:n]

# call function
# change number to however many words you want to see
common_words = get_top_n_words(text, 15)
with open('top_n_words.csv','w') as external_file:
    for word, freq in common_words:
        print((word, freq),file=external_file)
external_file.close
