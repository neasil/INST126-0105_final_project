# Import statements: 
from bs4 import BeautifulSoup
import requests
import numpy as np

# Prompting user to link to Wikipedia page
wiki_link = input("Please input a link to a Wikipedia page:\t").strip()

# Prompting user for words to count in the Wikipedia page
words = input("Please input words to count. You may enter as many you'd like. They should be separated by commas.\t").lower().strip()

# Converting inputted words into a list 
words_to_count = words.split(",")

# Removing any spaces in the words_to_count list 
fixed_words_count = np.array([])
for word in np.arange(len(words_to_count)):
    fixed_word = words_to_count[word].strip()
    fixed_words_count = np.append(fixed_words_count, fixed_word)
fixed_words_count

# Extracting URL
wiki_page = requests.get(wiki_link)

# Converting URL into readable HTML text
wiki_soup = BeautifulSoup(wiki_page.content, "html.parser")

# Converting HTML to readable text 
wiki_text = wiki_soup.get_text().lower()

# Making website text into a readable list
text_countable = wiki_text.split()

# Store counts of inputted words into an array
data = np.array([])
for w in np.arange(len(fixed_words_count)):
    print(fixed_words_count[w])
    counts = text_countable.count(fixed_words_count[w])
    data = np.append(data, counts)

# Printing results to user
data






