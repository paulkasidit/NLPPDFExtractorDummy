import os, json, string
import slate3k as slate

"""Extracting text from the PDF file and converting it to text format """
with open('/input/resume.pdf','rb')as f:
    doc = str(slate.PDF(f))

"""Loop to check if the path already exists, if not create a new folder with the output file inside"""
if not os.path.exists('/output'):
    os.mkdir('/output')

"""Writing the PDF output to a new file"""
path = '/output'
file = 'output.txt'
with open(os.path.join(path, file), 'w') as fp:
    fp.write(doc)

import nltk
nltk.download('punkt')
import re
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 

"""Opens the file in order to clean the text"""
f = open('output/output.txt','r+')
text_to_be_cleaned = f.readlines()

"""Cleaning the text"""
default_stemmer = PorterStemmer()
default_stopwords = stopwords.words('english') 

def CleanText(text):

    text = str(text_to_be_cleaned)

    def tokenize_text(text):
        return [w for s in sent_tokenize(text) for w in word_tokenize(s)]

    def remove_special_characters(text, characters=string.punctuation.replace('-', '')):
        tokens = tokenize_text(text)
        pattern = re.compile('[{}]'.format(re.escape(characters)))
        return ' '.join(filter(None, [pattern.sub('', t) for t in tokens]))

    def stem_text(text, stemmer=default_stemmer):
        tokens = tokenize_text(text)
        return ' '.join([stemmer.stem(t) for t in tokens])

    def remove_stopwords(text, stop_words=default_stopwords):
        tokens = [w for w in tokenize_text(text) if w not in stop_words]
        return ' '.join(tokens)

    text = text.strip(' ') # strip whitespaces
    text = text.lower() # lowercase
    """text = stem_text(text) # stemming"""
    text = remove_special_characters(text) # remove punctuation and symbols
    text = remove_stopwords(text) # remove stopwords
    #text.strip(' ') # strip whitespaces again?

    return text

"""Clears the original content(uncleaned text) and writes cleaned text to the same file."""
f.truncate(0)

f.write((CleanText(text_to_be_cleaned)))

from secrets import api_key
import requests 

#Parsing the Resume 
    #Authentication
    #Extract text from output.txt 


#writing the text to a json file (maybe?)
    #function to assign to relevant keys in "information.json"

