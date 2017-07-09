from __future__ import division
import nltk
from nltk.book import *

# Length of text
print(len(text3))

# Distinct  words
print(sorted(set(text3)))
print(len(set(text3)))

# Lexical Diversity
def lexical_diversity(text):
    return len(text) / len(set(text))

# Percentage of Lexical Diversity
def percentage(count, total):
    return 100 * count / total

print(lexical_diversity(text3))
print(percentage(text4.count('a'), len(text4)))
