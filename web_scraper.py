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

