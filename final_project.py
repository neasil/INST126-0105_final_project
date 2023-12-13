# Import statements: 
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Prompting user to link to Wikipedia page
wiki_link = input("Please input a link to a Wikipedia page:\t").strip()

# Prompting user for words to count in the Wikipedia page
words = input("Please input words to count. You may enter as many you'd like. They should be separated by commas.\t").lower().replace(".", ",").strip()

# Converting inputted words into a list 
words_to_count = words.split(",")

# Removing any spaces in the words_to_count list 
fixed_words_count = np.array([])
for word in np.arange(len(words_to_count)):
    fixed_word = words_to_count[word].strip()
    fixed_words_count = np.append(fixed_words_count, fixed_word)

# Extracting URL
wiki_page = requests.get(wiki_link)

# Converting URL into readable HTML text
wiki_soup = BeautifulSoup(wiki_page.content, "html.parser")

# Converting HTML to readable text 
wiki_text = wiki_soup.get_text().lower()

# Making website text into a readable list
text_countable = wiki_text.split()

# Storing data in a dictionary 
counts = {"Word": [], "Count": []}

# Store counts of inputted words into the dictionary
for w in np.arange(len(fixed_words_count)):
    print(fixed_words_count[w])
    count = text_countable.count(fixed_words_count[w])
    print(count)
    counts["Word"].append(fixed_words_count[w])
    counts["Count"].append(count)

# Converting the data in a data frame that can be plotted 
counts_table = pd.DataFrame.from_dict(counts)

# Asking the user how they would like to visualize their data
visualization = input("How would you like to visualize your data? Please enter either either 'scatterplot', 'barplot', or 'lineplot':\t").lower().strip()

# Visualizing the data based on whatever the user chooses
if visualization == "scatterplot":
    plt.scatter("Word", "Count", data = counts_table)
    plt.show()
elif visualization == "barplot":
    plt.bar("Word", "Count", data = counts_table)
    plt.show()
elif visualization == "lineplot":
    plt.plot("Word", "Count", data = counts_table)
    plt.show()


