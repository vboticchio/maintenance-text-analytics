from src.data_loader import load_data
from src.preprocessing import apply_preprocessing
from src.vectorization import create_vectorizer, vectorize_text
from src.modeling import train_svm
from src.criticidade import calculate_criticidade
from src.visualization import plot_top_terms

def main():

    df = load_data("data/dataset_2645.xlsx")
    df = apply_preprocessing(df)

    vectorizer = create_vectorizer()
    X_tfidf, terms = vectorize_text(vectorizer, df["texto_processado"])

    model = train_svm(X_tfidf, df["classe_evento"])
    df["rotulo_svm"] = model.predict(X_tfidf)

    df_terms = calculate_criticidade(df, X_tfidf, terms)

    plot_top_terms(df_terms)

if __name__ == "__main__":
    main()
