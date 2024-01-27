#4
import nltk
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, word_tokenize
def identify_nouns(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    print(tagged_words)
    nouns = [word for word, pos in tagged_words if pos.startswith('NN')]
    return nouns
sentence = "The quick brown fox jumps over the lazy dog."
nouns = identify_nouns(sentence)
if nouns:
    print("Nouns identified in the sentence:")
    for noun in nouns:
        if noun[-1].lower() in {'s', 'x', 'z'} or noun[-2:].lower() in {'ch', 'sh'}:
            print(noun+"es")
        else:
            print(noun+"s")
else:
    print("No nouns found in the sentence.")
