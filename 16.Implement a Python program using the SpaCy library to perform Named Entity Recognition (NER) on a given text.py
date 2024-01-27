#16
#spacy download en_core_web_sm
import spacy

nlp = spacy.load("en_core_web_sm")

text = "Apple is looking at buying U.K. startup for $1 billion"

doc = nlp(text)

for ent in doc.ents:
    print(f"Entity: {ent.text}, Type: {ent.label_}")
