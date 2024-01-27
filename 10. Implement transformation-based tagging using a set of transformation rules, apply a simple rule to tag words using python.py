#10
def apply_transformation_rule(word):
    # Apply a simple transformation rule (example rule: if a word ends with 'ing', tag it as a 'VERB')
    if word.lower().endswith('ing'):
        return 'VERB'
    else:
        return 'NOUN'
def transform_based_pos_tagging(sentence):
    tagged_sentence = []

    for word in sentence:
        pos_tag = apply_transformation_rule(word)
        tagged_sentence.append((word, pos_tag))

    return tagged_sentence

# Example sentence for transformation-based POS tagging
sentence_to_tag = ['The', 'running', 'dog', 'is', 'jumping']
# Perform transformation-based POS tagging
tagged_sentence = transform_based_pos_tagging(sentence_to_tag)
# Display the results
print("Original Sentence:", sentence_to_tag)
print("Transformation-based POS Tagging Result:", tagged_sentence)
