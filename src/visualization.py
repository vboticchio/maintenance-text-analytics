import matplotlib.pyplot as plt

def plot_top_terms(df_terms, top_n=15):
    top_terms = df_terms.head(top_n)

    cores = [
        "red" if c >= top_terms["criticidade"].median()
        else "orange"
        for c in top_terms["criticidade"]
    ]

    plt.figure(figsize=(10, 5))
    plt.barh(top_terms["termo"], top_terms["criticidade"], color=cores)
    plt.xlabel("Índice de criticidade")
    plt.ylabel("Termos técnicos")
    plt.title("Termos associados à maior criticidade de parada")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
