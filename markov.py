"""Generate Markov text from text files."""

from random import choice
import sys
import pdb

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path)
    contents = file.read()
    file.close()

    return contents


def open_and_read_files(file_path1, file_path2):
    file1 = open(file_path1)
    file2 = open(file_path2)

    content1 = file1.read()
    content2 = file2.read()

    file1.close()
    file2.close()

    return content1 + content2


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
Notes: 
for i in range(len(words)-2): we got the length of the whole list . going up to
 minus 2 so we don't get index error
 # taking the entire text and splitting at white spaces
# create a tuple
# function is making a tuple(key) to list(value) dictonary
# words is a list and each word is an element. so we split at the white spaces
#     chains[word_tuple] = []
        chains[word_tuple].append(value)
         if the word is not in the dictonaries key  its adding an empty list to
 
    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()
    for i in range(len(words)-2):
        word_tuple = (words[i], words[i + 1])
        value = words[i + 2]
        if word_tuple not in chains:
            chains[word_tuple] = []
        chains[word_tuple].append(value)

    # your code goes here

    return chains


def make_n_chains(text_string, n):
    chains = {}
    words = text_string.split()
    for i in range(len(words)-n):
        list_for_tuple = words[i:i+n]
        word_tuple = tuple(list_for_tuple)
        value = words[i + n]
        if word_tuple not in chains:
            chains[word_tuple] = []
        chains[word_tuple].append(value)
    # pdb.set_trace()
    return chains


def make_n_text(chains):
    words = []
    current_key = choice(list(chains.keys()))
    n = len(current_key)
    chosen_word = choice(chains[current_key])
    for word in current_key:
        words.append(word)
    words.append(chosen_word)

    while chosen_word is not None:
        key_list = list(current_key[1:])
        key_list.append(chosen_word)
        current_key = tuple(key_list)
        if current_key in chains:
            chosen_word = choice(chains[current_key])
        else:
            chosen_word = None
    #pdb.set_trace()
    return " ".join(words)



def make_text(chains):
    """Return text from chains."""
# we got a random key and random word from the key value
# initalize
    words = []
    current_key = choice(list(chains.keys()))

    # pdb.set_trace()
    chosen_word = choice(chains[current_key])
    for word in current_key:
        words.append(word)
    words.append(chosen_word)
    # reassign the current_key variable to the first key
    while chosen_word is not None:
        current_key = (current_key[1], chosen_word)
        if current_key in chains:
            chosen_word = choice(chains[current_key])
            for word in current_key:
                words.append(word)
            words.append(chosen_word)
        else:
            chosen_word = None

    # your code goes here

    return " ".join(words)


def make_sentences(chains):
    """Return text from chains."""
# we got a random key and random word from the key value
# initalize
    words = []
    current_key = choice(list(chains.keys()))
    while not (current_key[0][0].isupper() and current_key[1][0].islower()):
        current_key = choice(list(chains.keys()))

    #pdb.set_trace()
    chosen_word = choice(chains[current_key])
    for word in current_key:
        words.append(word)
    words.append(chosen_word)
    # reassign the current_key variable to the first key
    while chosen_word is not None:
        current_key = (current_key[1], chosen_word)
        if current_key in chains:
            chosen_word = choice(chains[current_key])
            for word in current_key:
                words.append(word)
            words.append(chosen_word)
        else:
            chosen_word = None

    return " ".join(words)


input_path = "green-eggs.txt"
input_path2 = "gettysburg.txt"
if len(sys.argv) > 1:
    input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_files(input_path, input_path2)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_sentences(chains)

print(random_text)
