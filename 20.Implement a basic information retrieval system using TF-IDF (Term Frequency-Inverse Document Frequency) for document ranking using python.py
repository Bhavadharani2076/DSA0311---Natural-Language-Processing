#20
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

query = "this is the second document"

query_vector = vectorizer.transform([query])

cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

document_scores = [(score, doc) for score, doc in zip(cosine_similarities, documents)]
sorted_documents = sorted(document_scores, key=lambda x: x[0], reverse=True)

print("Ranked documents based on TF-IDF similarity to the query:")
for i, (score, doc) in enumerate(sorted_documents, start=1):
    print(f"Rank {i}: Similarity Score: {score:.4f}, Document: '{doc}'")
