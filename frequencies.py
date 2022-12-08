"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    temp = list(map(str, items))
    for element in temp:
        frequencies[element] = frequencies.get(element, 0) + 1
    return frequencies

input = ['0', 4,4,'4','d','d','e',0,'a','d','4']
print(frequencies(input))
