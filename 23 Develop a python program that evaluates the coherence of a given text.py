#23

import nltk

def calculate_coherence(text):
    sentences = nltk.sent_tokenize(text)
    coherence_markers = ['however', 'therefore', 'consequently', 'nevertheless', 'furthermore', 'meanwhile', 'although', 'while', 'yet', 'moreover']

    total_markers = 0
    for sentence in sentences:
        tokenized_sentence = nltk.word_tokenize(sentence.lower())
        for marker in coherence_markers:
            if marker in tokenized_sentence:
                total_markers += 1

    return total_markers

text = "The weather was terrible. However, they decided to go for a picnic. Therefore, they packed their bags and left."

coherence_score = calculate_coherence(text)
print(f"Coherence Score: {coherence_score}")
