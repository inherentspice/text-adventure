import requests
from bs4 import BeautifulSoup
import pandas as pd


link = 'https://www.truity.com/test/type-finder-personality-test-new'
webpage_response = requests.get(link)
webpage = webpage_response.content
soup = BeautifulSoup(webpage,'html.parser')

spans = set(soup.find_all('span', attrs={'class':"label-text"}))
    
with open("processed.csv", "w") as external_file:
    for span in spans:
        if span.get_text("|").split("|")[:-1] != ['E-mail '] and span.get_text("|").split("|")[:-1] != ['Password ']:
            if span.get_text("|").split("|")[:-1] != []:
                print(span.get_text("|").split("|")[:-1], file=external_file)
            else:
                pass
    external_file.close()

