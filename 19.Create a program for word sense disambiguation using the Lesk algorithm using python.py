#19
import nltk
nltk.download('stopwords')
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
def lesk_algorithm(word, sentence):
    best_sense = None
    max_overlap = 0
    word = word.lower()
    context = set(word_tokenize(sentence.lower()))
    context = context.difference(set(stopwords.words('english')))
    synsets = wordnet.synsets(word)
    for sense in synsets:
        signature = set(word_tokenize(sense.definition()))
        signature = signature.union(set([word.lower() for word in sense.lemma_names()]))
        overlap = len(context.intersection(signature))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense
    return best_sense
sentence = "I went to the bank to deposit money."
target_word = "bank"
sense = lesk_algorithm(target_word, sentence)
if sense:
    print(f"Target word: {target_word}")
    print(f"Best sense: {sense.name()} - Definition: {sense.definition()}")
else:
    print(f"No suitable sense found for '{target_word}' in the context of the sentence.")
