import nltk
import re
import pprint
from nltk import word_tokenize

import urllib2

#Adam Smith's Wealth of Nations
url = 'http://www.gutenberg.org/cache/epub/3300/pg3300.txt'
response = urllib2.urlopen(url)
#converts response to a string assuming utf8 encoding
raw = response.read().decode('utf8')

#slice out license info, header, etc.
start = raw.find('*** START OF THIS PROJECT GUTENBERG EBOOK')
end = raw.rfind('*** END OF THIS PROJECT GUTENBERG EBOOK')
raw = raw[start:end]

#returns list of all words used in raw converted to lowercase
tokens = [w.lower() for w in word_tokenize(raw)]
vocab = sorted(set(tokens))
