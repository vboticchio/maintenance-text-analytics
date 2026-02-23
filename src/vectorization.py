from sklearn.feature_extraction.text import TfidfVectorizer

def create_vectorizer():
    return TfidfVectorizer(
        max_features=3000,
        ngram_range=(1, 2)
    )

def vectorize_text(vectorizer, texts):
    X = vectorizer.fit_transform(texts)
    terms = vectorizer.get_feature_names_out()
    return X, terms
