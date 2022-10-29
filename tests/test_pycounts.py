#!/usr/bin/env python

"""Tests for `pycounts` package."""

from pycounts.pycounts import count_words
from collections import Counter

def test_count_words():
    """Test word counting from a file."""
    expected = Counter({
        'over': 2, 'and': 2, 'insanity': 1, 'is': 1, 'doing': 1,
        'the': 1, 'same': 1, 'thing': 1, 'expecting': 1,
        'different': 1, 'results': 1})
    actual = count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote counted incorrectly!"