"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    str(items)
    for element in items:
        frequencies[element] = frequencies.get(element, 0) + 1
    return frequencies


