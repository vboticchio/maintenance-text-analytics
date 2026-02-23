import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("portuguese"))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    tokens = [t for t in text.split() if t not in stop_words]
    return " ".join(tokens)

def apply_preprocessing(df):
    df["texto_processado"] = df["descricao"].apply(preprocess_text)
    return df
