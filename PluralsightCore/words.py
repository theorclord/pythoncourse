#!/usr/bin/python
"""Retrieve and print words from a URL.

Usage: 

    python words.py <URL>
"""

from urllib.request import urlopen
import sys


#'http://sixty-north.com/c/t.txt'

def fetchWords(url):
    """Fetch a list of words from a URL.
    
        Args:
            url: The URL of a UTF-8 text document.
            
        Returns:
            A list of strings containing the words from
            the document.
    """
    story = urlopen(url)
    storyWords = []

    for line in story:
        lineWords = line.decode('utf8').split()
        for word in lineWords:
                storyWords.append(word)

    story.close()
    return storyWords

def printItems(items):
    """Print items one per line.

        Args:
            An itereable series of printable items.
    """
    for item in items:
        print(item)

def main(url):
    """Print each word from a text document from a URL.

        Args:
            url: The URL of a UTF-8 text document.
    """
    words = fetchWords(url)
    printItems(words)

# run if this is run as a script
if __name__ == "__main__":
    main(sys.argv[1]) # the 0th arg is the module filename.