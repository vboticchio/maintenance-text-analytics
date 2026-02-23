import pandas as pd

def load_data(path):
    df = pd.read_excel(path)
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=["descricao", "tempo_parada", "classe_evento"])
    return df
