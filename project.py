import requests
from bs4 import BeautifulSoup

#Scraping first page of seven-page survey

link = 'https://www.truity.com/test/type-finder-personality-test-new'
webpage_response = requests.get(link)
webpage = webpage_response.content
soup = BeautifulSoup(webpage,'html.parser')

spans = set(soup.find_all('span', attrs={'class':"label-text"}))
    
with open("five_options_questions.csv", "w") as external_file:
    for span in spans:
        if span.get_text("|").split("|")[:-1] != ['E-mail '] and span.get_text("|").split("|")[:-1] != ['Password ']:
            if span.get_text("|").split("|")[:-1] != []:
                print(str(span.get_text("|").split("|")[:-1][0]), file=external_file)
            else:
                pass

#scraping rest of the pages through saving locally
def get_questions(filename,docname):
    with open(filename) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        spans = set(soup.find_all('span', attrs={'class':"label-text"}))
    with open(docname, "a") as external_file:
        for span in spans:
            if span.get_text("|").split("|")[:-1] != ['E-mail '] and span.get_text("|").split("|")[:-1] != ['Password ']:
                if span.get_text("|").split("|")[:-1] != []:
                    print(str(span.get_text("|").split("|")[:-1][0]), file=external_file)
                else:
                    pass
        external_file.close()


filenames=['2.html','3.html','4.html','5.html']
for file in filenames:
    get_questions(file,'five_options_questions.csv')


with open('6.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    spans = soup.find_all('label', attrs={'class':"control-label"})
with open("choose_one.csv", "w") as external_file:
    for span in spans[2:-1]:
        for child in set(span.children):
            if len(child.get_text())>2:
                print(str(child.get_text().strip("*")),file=external_file)

from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv

#preprocess csv
text = []
with open('five_options_questions.csv', 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        text.append(row)

# load text that you want to count word frequencies


# # function that tokenizes, removes stop words, vectorizers, and counts the most common words
# def get_top_n_words(text, n=None):
#     """
#     List the top n words in a vocabulary according to occurrence in a text without very common words.
#
#     get_top_n_words('fish, flew dangerously far toward the flying fly for only the
#     fly near a flying fish is truly a fly, 2')
#     -->
#     [('fly', 3),
#     ('fish', 2)]
#     """
#     tokenized = word_tokenize(text)
#     stop_words = set(stopwords.words('english'))
#     filtered_sentence = []
#
#     for t in tokenized:
#         if t not in stop_words:
#             filtered_sentence.append(t)
#     vec = CountVectorizer().fit(filtered_sentence)
#     bag_of_words = vec.transform(filtered_sentence)
#     sum_words = bag_of_words.sum(axis=0)
#     words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
#     words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
#     return words_freq[:n]
#
# # call function
# # change number to however many words you want to see
# common_words = get_top_n_words(text, 20)
# for word, freq in common_words:
#     print(word, freq)
