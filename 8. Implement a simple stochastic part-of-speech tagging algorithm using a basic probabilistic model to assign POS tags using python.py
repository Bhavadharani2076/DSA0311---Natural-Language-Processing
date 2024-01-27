#8
import random
def train_unigram_model(tagged_corpus):
    unigram_model = {}

    for sentence in tagged_corpus:
        for word, pos_tag in sentence:
            if word in unigram_model:
                unigram_model[word].append(pos_tag)
            else:
                unigram_model[word] = [pos_tag]
    return unigram_model
def stochastic_pos_tagging(sentence, unigram_model):
    tagged_sentence = []

    for word in sentence:
        if word in unigram_model:
            pos_tag = random.choice(unigram_model[word])
        else:
            pos_tag = 'NOUN'

        tagged_sentence.append((word, pos_tag))

    return tagged_sentence
tagged_corpus = [
    [('The', 'DET'), ('quick', 'ADJ'), ('brown', 'ADJ'), ('fox', 'NOUN')],
    [('Jumped', 'VERB'), ('over', 'PREP'), ('the', 'DET'), ('lazy', 'ADJ'), ('dog', 'NOUN')]
]
unigram_model = train_unigram_model(tagged_corpus)
sentence_to_tag = ['The', 'lazy', 'fox', 'jumped']
tagged_sentence = stochastic_pos_tagging(sentence_to_tag, unigram_model)
print("Original Sentence:", sentence_to_tag)
print("Stochastic POS Tagging Result:", tagged_sentence)
