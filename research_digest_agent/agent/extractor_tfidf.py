from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

nltk.download('punkt')

def extract_claims_tfidf(text, top_n=5):
    sentences = nltk.sent_tokenize(text)

    if len(sentences) < 2:
        return []

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)

    scores = tfidf_matrix.sum(axis=1)

    ranked_sentences = sorted(
        [(scores[i, 0], sentences[i]) for i in range(len(sentences))],
        reverse=True
    )

    claims = []
    for score, sentence in ranked_sentences[:top_n]:
        claims.append({
            "claim": sentence,
            "evidence": sentence[:150],
            "score": float(score)
        })

    return claims