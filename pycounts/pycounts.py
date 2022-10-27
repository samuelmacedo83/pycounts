from collections import Counter
from string import punctuation

def load_text(input_file):
    """Load text from a text file and return as a styring."""
    with open(input_file, encoding="utf-16") as file:
        text = file.read()
    return text

def clean_text(text):
    """Lowercase and remove puctuation from a string. """
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text

def count_words(input_file):
    """Count unique words in a string."""
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)