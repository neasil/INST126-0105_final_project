# Import statements: 
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Welcome message:
print("Welcome! This is a simple program that allows you to count how many times certain words appear in Wikipedia articles and calculate the proportion of times they appear in the text. \n\nBut also...You get to see how that compares to the Bee Movie's script!")
print("That's not all! The words you count will also be visualized in a plot of your choice. \n\nNow with all of that said, let's begin!")

# Prompting the user to enter a link to a Wikipedia page
wiki_link = input("Please input a link to a Wikipedia page:\t").strip()

# Checking that the user actually entered a link to a Wikipedia article
if "wikipedia" not in wiki_link:
    wiki_link = input("This program only takes links to Wikipedia articles. Please input a link to a Wikipedia page:\t").strip()
    if "wikipedia" not in wiki_link:
        print("You have failed to provide an acceptable link. The program will now close.")
        exit()

# Prompting user for words to count in the Wikipedia page
words = input("Please input words to count. You may enter as many you'd like. They should be separated by commas.\t").lower().replace(".", ",").strip()

# Converting inputted words into a list 
words_to_count = words.split(",")

# Cleaning up the words_to_count list 
fixed_words_count = np.array([])
for word in np.arange(len(words_to_count)): 
    # Iterating through every inputted word to remove white space and storing in a new array
    fixed_word = words_to_count[word].strip() 
    fixed_words_count = np.append(fixed_words_count, fixed_word)

# Extracting URL so we can get the webpage's text
wiki_page = requests.get(wiki_link) # 10.1

# Converting URL into HTML text
wiki_soup = BeautifulSoup(wiki_page.content, "html.parser") # 10.2

# Converting HTML into more readable text 
wiki_text = wiki_soup.get_text().lower() # 10.3

# Changing text into a parsable list
text_countable = wiki_text.split()

# Preparing a dictionary to store the counts of each word
counts = {"Word": [], "Count": []}

# Storing counts of inputted words into the dictionary
for word in np.arange(len(fixed_words_count)):
    # Iterating through every word in the fixed_words_count list and counting the number of times they appear
    count = text_countable.count(fixed_words_count[word])
    # Adding each word and its corresponding count to the dictionary
    counts["Word"].append(fixed_words_count[word])
    counts["Count"].append(count)

# Converting the dictionary into a dataframe that can be plotted 
counts_table = pd.DataFrame.from_dict(counts)

# Calculating the proportions of each word's number of occurences 
counts_prop = counts_table["Count"] / len(text_countable) # 8.1

# Creating a new column for the calculated proportions
counts_table["Proportion"] = counts_prop

# Writing the user's results to a .csv file
counts_table.to_csv("word_counts.csv", index = False) # 8.4

# Printing out the user's results 
word_counts = pd.read_csv("word_counts.csv") # 8.2
print(word_counts)
print("Your data has been stored in a file named 'word_counts.csv.'")
print("\n")


#############################################

# Time to scrape the Bee Movie's text!
print("But how does this compare to the Bee Movie script?")

# Extracting URL
bee_page = requests.get("https://courses.cs.washington.edu/courses/cse163/20wi/files/lectures/L04/bee-movie.txt")

# Converting URL into HTML text
bee_soup = BeautifulSoup(bee_page.content, "html.parser")

# Converting HTML into more readable text 
bee_text = bee_soup.get_text().lower()

# Changing text into a parsable list
bee_script = bee_text.split()

# Preparing a dictionary to store the counts of each word
bee_counts = {"Word": [], "Count": []}

# Storing counts of inputted words into the dictionary
for word in np.arange(len(fixed_words_count)):
    # Iterating through every word in the fixed_words_count list and counting the number of times they appear
    bee_count = bee_script.count(fixed_words_count[word])
    # Adding each word and its corresponding count to the dictionary
    bee_counts["Word"].append(fixed_words_count[word])
    bee_counts["Count"].append(bee_count)

# Converting the dictionary into a dataframe that can be plotted 
bee_counts_table = pd.DataFrame.from_dict(bee_counts)

# Calculating the proportions of each word's number of occurences 
bee_counts_prop = bee_counts_table["Count"] / len(bee_script) 

# Creating a new column for the calculated proportions
bee_counts_table["Proportion"] = bee_counts_prop

# Showing the user the table for the Bee Movie
print(bee_counts_table)

# Comparing the user's data to the Bee Movie's: 
# Checking for proportions of user's data that are larger than the Bee Movie's proportions
greater_than = counts_table[counts_table["Proportion"] > bee_counts_table["Proportion"]] # 8.3
print("The Wikipedia page had a larger proportion of these words than the Bee Movie's.\n")
print(greater_than)
print("\n")
# Checking for proportions of user's data that are smaller than the Bee Movie's proportions
less_than = counts_table[counts_table["Proportion"] < bee_counts_table["Proportion"]]
print("The Wikipedia page has a smaller proportions of these words than the Bee Movie's.\n")
print(less_than)
print("\n")

# Asking the user how they would like to visualize their data
visualization = input("How would you like to visualize your data? Please enter either 'scatterplot', 'barplot', or 'lineplot':\t").lower().strip()

# Checking if the user input either 'scatterplot', 'barplot', or 'lineplot'
if visualization != "scatterplot" and visualization != "barplot" and visualization != "lineplot":
    # Giving the user a second chance to re-enter their answer
    visualization = input("You have entered an invalid input. Please remember to enter either 'scatterplot', 'barplot', or 'lineplot'.\t").lower().strip()
    if visualization != "scatterplot" and visualization != "barplot" and visualization != "lineplot":
        # If the user fails a second time, the program quits automatically 
        print("You have failed to enter a valid input. The program will now close.")
        exit()

# Visualizing the data based on whatever the user chooses:
if visualization == "scatterplot":
    # Graphing a scatter plot
    plt.scatter("Word", "Count", color = "r", data = counts_table)
    plt.scatter("Word", "Count", color = "g", data = bee_counts_table)
    plt.show()
elif visualization == "barplot": # https://www.geeksforgeeks.org/plotting-multiple-bar-charts-using-matplotlib-in-python/
    # Graphing a bar plot
    x = counts_table["Word"].values
    ycounts = counts_table["Count"].values
    ybee = bee_counts_table["Count"].values

    x_axis = np.arange(len(x)) 
    
    # Making it so we can see both plots for both datasets on the same graph
    plt.bar(x_axis - 0.2, ycounts, 0.4, label = wiki_link, color = "r") 
    plt.bar(x_axis + 0.2, ybee, 0.4, label = "Bee Movie Script", color = "g") 

    plt.xticks(x_axis, x) 
    plt.xlabel("Words") 
    plt.ylabel("Count") 
    plt.title("Wikipedia Page v.s. Bee Movie Script") 
    plt.legend() 
    plt.show()
elif visualization == "lineplot":
    # Graphing a line plot
    plt.plot("Word", "Count", color = "r", data = counts_table)
    plt.plot("Word", "Count", color = "g", data = bee_counts_table)
    plt.show()

# Closing the program!
exit()