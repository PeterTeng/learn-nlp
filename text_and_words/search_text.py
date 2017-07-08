import nltk
# Need to download books data with nltk.download()
from nltk.book import *

#
# Search text
# ------------------------------
# Concordance: search text with words around it
print(text1.concordance("monstrous"))

# Similar: search for all similar words
print(text1.similar("monstrous"))

# Common Contexts: search words with same usage contexts
print(text2.common_contexts(["monstrous", "very"]))

# Dispersion Plot: word usage in plot graph
# required numpy and matplotlib
print(text4.dispersion_plot(["citizens", "freedom", "war", "terrorist", "love", "America"]))
