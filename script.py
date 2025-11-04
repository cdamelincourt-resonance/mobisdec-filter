import pandas as pd
import requests
import io
from datetime import datetime
import os

# Télécharger le fichier CSV
url = "https://www.data.gouv.fr/api/1/datasets/r/eb76d20a-8501-400e-b336-d85724de5435"
response = requests.get(url)
response.raise_for_status()

# Lire le CSV
df = pd.read_csv(io.StringIO(response.text), sep=',', low_memory=False)

# Filtrer
filtered = df[df['nom_enseigne'] == 'MobiSDEC']

# Créer le dossier output s'il n'existe pas
os.makedirs("output", exist_ok=True)

# Sauvegarder le fichier filtré
filename = f"output/mobisdec_{datetime.today().strftime('%Y%m%d')}.csv"
filtered.to_csv(filename, index=False)
