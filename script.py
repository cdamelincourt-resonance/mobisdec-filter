import pandas as pd
import requests
import io

# Télécharger le fichier CSV
url = "https://www.data.gouv.fr/api/1/datasets/r/eb76d20a-8501-400e-b336-d85724de5435"
response = requests.get(url)
df = pd.read_csv(io.StringIO(response.text), sep=',', low_memory=False)

# Filtrer les lignes
filtered = df[df['nom_enseigne'] == 'MobiSDEC']

# Sauvegarder le résultat
filtered.to_csv("mobisdec_filtré.csv", index=False)
