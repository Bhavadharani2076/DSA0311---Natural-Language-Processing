#6
import random
def build_bigram_model(sentences):
    bigram_model = {}
    for sentence in sentences:
        tokens = sentence.split()
        for i in range(len(tokens) - 1):
            current_word = tokens[i]
            next_word = tokens[i + 1]
            if current_word in bigram_model:
                bigram_model[current_word].append(next_word)
            else:
                bigram_model[current_word] = [next_word]
    return bigram_model
def generate_text(bigram_model, start_word, length=10):
    generated_text = [start_word]
    for _ in range(length - 1):
        if start_word in bigram_model:
            next_word = random.choice(bigram_model[start_word])
            generated_text.append(next_word)
            start_word = next_word
        else:
            break
    
    return ' '.join(generated_text)
sentences = [
    "I love programming in Python.",
    "Python is a versatile programming language.",
    "Text generation using bigram models is interesting.",
    "Natural Language Processing involves analyzing and generating text."
]
bigram_model = build_bigram_model(sentences)
print(bigram_model)
generated_text = generate_text(bigram_model, start_word="I", length=8)
print("Generated Text:", generated_text)
