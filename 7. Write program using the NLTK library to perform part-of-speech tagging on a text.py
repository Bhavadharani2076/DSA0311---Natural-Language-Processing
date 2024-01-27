#7
import nltk
from nltk import pos_tag, word_tokenize
def perform_pos_tagging(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    # Perform part-of-speech tagging
    tagged_words = pos_tag(words)
    return tagged_words
# Example text
text = "NLTK is a powerful library for natural language processing."
# Perform part-of-speech tagging
tagged_words = perform_pos_tagging(text)

print("Original Text:", text)
print("Part-of-Speech Tagging Result:", tagged_words)
