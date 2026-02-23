import numpy as np
import pandas as pd

def calculate_criticidade(df, X_tfidf, terms):
    tfidf_mean = np.asarray(X_tfidf.mean(axis=0)).flatten()

    df_terms = pd.DataFrame({
        "termo": terms,
        "peso_tfidf": tfidf_mean
    })

    criticidade = []

    for termo in df_terms["termo"]:
        mask = df["texto_processado"].str.contains(termo, regex=False)
        tempo_medio = df.loc[mask, "tempo_parada"].mean()
        peso = df_terms.loc[df_terms["termo"] == termo, "peso_tfidf"].values[0]
        score = peso * tempo_medio if not np.isnan(tempo_medio) else 0
        criticidade.append(score)

    df_terms["criticidade"] = criticidade
    return df_terms.sort_values(by="criticidade", ascending=False)
