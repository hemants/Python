"""Retrieve and print words from a URL.

Usage:
    python words.py <url>
"""

# python 3 example
# Also for below code while doign a import we can do following
# >>> from words import (fetch_words, print_words, main)
# >>> from words import *
# test url: http://sixty-north.com/c/t.txt
from urllib.request import urlopen
import sys


def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of string contaning the words.
    """
    with urlopen(url) as response:
        #print(type(response))
        story_words = []
        for line in response:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Prints an item from list.

    Args:
        items: The list of item.
    """
    for item in items:
        print(item)


def main(url):
    """Prints each word from the document returned by url.

    Args:
        url: the document url.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) # this a way to access command line arguments, need to import sys module