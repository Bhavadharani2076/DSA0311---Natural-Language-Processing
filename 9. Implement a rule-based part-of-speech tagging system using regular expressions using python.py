#9
import re
def rule_based_pos_tagging(sentence):
    tagged_sentence = []
    for word in sentence:
        if re.match(r'\b(?:is|am|are|was|were)\b', word, re.IGNORECASE):
            pos_tag = 'VERB'
        elif re.match(r'\b(?:the|a|an)\b', word, re.IGNORECASE):
            pos_tag = 'DET'
        elif re.match(r'\b(?:quick|brown|lazy)\b', word, re.IGNORECASE):
            pos_tag = 'ADJ'
        else:
            pos_tag = 'NOUN'

        tagged_sentence.append((word, pos_tag))
    return tagged_sentence
# Example sentence for rule-based POS tagging
sentence_to_tag = ['The', 'quick', 'brown', 'fox', 'is', 'lazy']
# Perform rule-based POS tagging
tagged_sentence = rule_based_pos_tagging(sentence_to_tag)
# Display the results
print("Original Sentence:", sentence_to_tag)
print("Rule-based POS Tagging Result:", tagged_sentence)
