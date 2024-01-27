#21
import spacy
nlp = spacy.load("en_core_web_sm")
def syntax_semantic_analysis(sentence):
    doc = nlp(sentence)
    noun_phrases_and_meanings = []
    for chunk in doc.noun_chunks:
        head_word = chunk.root.text
        head_meaning = get_word_meaning(head_word)
        noun_phrases_and_meanings.append({
            'noun_phrase': chunk.text,
            'meaning': head_meaning
        })

    return noun_phrases_and_meanings
def get_word_meaning(word):
    return f"Dummy meaning for {word}"
sentence = "The quick brown fox jumps over the lazy dog."
results = syntax_semantic_analysis(sentence)
for result in results:
    print(f"Noun Phrase: {result['noun_phrase']}, Meaning: {result['meaning']}")
