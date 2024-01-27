#13
import nltk
from nltk import CFG

# Define a context-free grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> 'John'
    VP -> V NP
    V -> 'likes'
    NP -> 'pizza'
""")

# Create a parser based on the grammar
parser = nltk.ChartParser(grammar)

# Given sentence
sentence = "John likes pizza"

# Tokenize the sentence
tokens = sentence.split()

# Generate and print parse trees
for tree in parser.parse(tokens):
    tree.pretty_print()
