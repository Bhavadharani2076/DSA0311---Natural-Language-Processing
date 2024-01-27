#3
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
def perform_morphological_analysis(text):
    # Tokenize the input text into words
    words = word_tokenize(text)
    print(words)
    # Initialize the Porter Stemmer
    porter_stemmer = PorterStemmer()
    print(porter_stemmer)
    # Perform stemming for each word
    stemmed_words = [porter_stemmer.stem(word) for word in words]
    return stemmed_words

# Example text for morphological analysis
input_text = "Running and played are both verb forms of the word run and play."

# Perform morphological analysis
result = perform_morphological_analysis(input_text)
# Display the results
print("Original Text:")
print(input_text)
print("\nMorphological Analysis:")
print(result)
