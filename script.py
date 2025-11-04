import pandas as pd

# Télécharger le fichier CSV
url = "https://www.data.gouv.fr/api/1/datasets/r/eb76d20a-8501-400e-b336-d85724de5435"
df = pd.read_csv(url, sep=';', low_memory=False)

# Filtrer les lignes
filtered_df = df[df['nom_enseigne'] == 'MobiSDEC']

# Enregistrer le fichier filtré
filtered_df.to_csv("mobisdec_filtré.csv", index=False)
