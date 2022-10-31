from collections import Counter
from string import punctuation

def load_text(input_file):
    """Load text from a text file and return as a styring.
    
    Parameters
    ----------
    input_file : str
        Path to text file.

    Returns
    -------
    str
        Text file contents.

    Examples
    --------
    >>> load_text("zen.txt")    
    """
    with open(input_file) as file:
        text = file.read()
    return text

def clean_text(text):
    """Lowercase and remove puctuation from a string.
    
    Parameters
    ----------
    text : str
        Text to clean.

    Returns
    -------
    str
        Clean text.

    Examples
    --------
    >>> clean_text("Early optimization is the root os all evil!")
    'early optimization is the root of all evil'    
    """
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text

def count_words(input_file):
    """Count unique words in a text file.
    
    Words are made lowercase and punctuation is removed
    before counting.

    Parameters
    ----------
    input_file : str
        Path to the file.

    Returns
    -------
    collections.Counter
        dict-like object where keys are words and values
        are counts.

    Examples
    --------
    >>> count_words("zen.txt")
    """
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)