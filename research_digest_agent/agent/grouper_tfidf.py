from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def group_claims_tfidf(all_claims, num_clusters=3):
    if not all_claims:
        return []

    texts = [c["claim"] for c in all_claims]

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)

    num_clusters = min(num_clusters, len(texts))

    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    labels = kmeans.fit_predict(X)

    groups = {}
    for i, label in enumerate(labels):
        groups.setdefault(label, []).append(all_claims[i])

    return list(groups.values())