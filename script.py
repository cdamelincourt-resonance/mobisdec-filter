import pandas as pd

# URL du fichier CSV
url = "https://www.data.gouv.fr/api/1/datasets/r/eb76d20a-8501-400e-b336-d85724de5435"

# Lire le CSV directement depuis l'URL
df = pd.read_csv(url, sep=';', low_memory=False)

# Filtrer les lignes où nom_enseigne == "MobiSDEC"
filtered_df = df[df['nom_enseigne'] == 'MobiSDEC']

# Sauvegarder le résultat dans un nouveau fichier CSV
filtered_df.to_csv("mobisdec_filtré.csv", index=False)
