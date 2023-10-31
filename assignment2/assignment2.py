import random
import urllib.request
import string
import sys
from thefuzz import fuzz 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from unicodedata import category

# Part 1: Harvesting and Reading the data

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    freq = {}
    fp = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(fp)

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            freq[word] = freq.get(word, 0) + 1

    return freq

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

# Part 2: Analyze the Text

# def word_count(filename, word):
#     """
#     This function finds how many 
#     """
#     count = 0 
#     words = text.split()
#     # Open file in read mode
#     with open(filename, 'r') as file:
#         text = file.read()
#     for word in words:
#         if word.lower() == "the":
#             count += 1
#     return count

# answer = (word_count("Peter_Pan.txt","the"))
# print(f'The word "the" appears {answer} times in the text.')

def word_count(filename, word):
    # Open file in read mode
    with open(filename, 'r') as file:
        # Read the content of the file
        text = file.read()
    
    # Using count()
    return text.count(word)

result = word_count('Peter Pan.txt', 'the')
print(f'The word "the" appears {result} times in the text.')

# def total_amount_words(freq):
#     """
#     This function will find the total frequency 
#     """
#     return sum(freq.values())

# def most_common(hist):
#     """
#     This function is used to calculate the 20 most common words 
#     occuring in the Peter Pan text.
#     """
#     common = []
#     for word, val in hist.items():
#         common.append((val, word))
#     common.sort(reverse=True)
#     for freq, word in common[0:20]:
#         print(word, '\t', freq)

# # Part 3: Natural Language Processing
# # Part 4: Text Similarity
# def main():
#     hist = process_file('data/Peter Pan.txt', skip_header=True)
#     # print(hist)
#     # print('Total number of words:', total_words(hist))
#     # print('Number of different words:', different_words(hist))

#     # t = most_common(hist, excluding_stopwords=True)
#     # print('The most common words are:')
#     # for freq, word in t[0:20]:
#     #     print(word, '\t', freq)

#     # words = process_file('words.txt', skip_header=False)

#     # diff = subtract(hist, words)
#     # print("The words in the book that aren't in the word list are:")
#     # for word in diff.keys():
#     #     print(word, end=' ')

#     # print("\n\nHere are some random words from the book")
#     # for i in range(100):
#     #     print(random_word(hist), end=' ')


# if __name__ == '__main__':
#     main()