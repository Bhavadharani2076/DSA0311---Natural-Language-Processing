#22
import nltk

def resolve_references(text):
    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]

    resolved_text = []
    pronouns = set(['he', 'him', 'his', 'she', 'her', 'it', 'they', 'them', 'their'])

    for tagged_sentence in tagged_sentences:
        resolved_sentence = []
        for word, pos in tagged_sentence:
            if word.lower() in pronouns and len(resolved_sentence) > 0:
                antecedent = resolved_sentence[-1]
                resolved_sentence.append(f'({word} -> {antecedent})')
            else:
                resolved_sentence.append(word)
        resolved_text.append(' '.join(resolved_sentence))

    return ' '.join(resolved_text)

text = "John went to the market and He bought some fruits."

resolved_text = resolve_references(text)
print(resolved_text)
