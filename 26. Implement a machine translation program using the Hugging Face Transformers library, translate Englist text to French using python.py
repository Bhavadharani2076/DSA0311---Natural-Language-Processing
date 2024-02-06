#26
from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
result = translator("Hello, how are you?")
print(result[0]['translation_text'])
