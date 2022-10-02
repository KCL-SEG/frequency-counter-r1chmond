"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for element in items:
        frequencies[element] = frequencies.get(element, 0) + 1
    return frequencies

