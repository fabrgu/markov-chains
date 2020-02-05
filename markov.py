"""Generate Markov text from text files."""

from random import choice
import pdb

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

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
# taking the entire text and splitting at white spaces
# create a tuple
# function is making a tuple(key) to list(value) dictonary

    words = text_string.split()
    for i in range(len(words)-2):
        word_tuple = (words[i], words[i + 1])
        value = words[i + 2]
        if word_tuple not in chains:
            chains[word_tuple] = []
        chains[word_tuple].append(value)

    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""
# we got a random key and random word from the key value
# initalize
    words = []
    pdb.set_trace()
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


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
