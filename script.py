import pandas as pd
import requests
import io
from datetime import datetime

# Télécharger le fichier CSV
url = "https://www.data.gouv.fr/api/1/datasets/r/eb76d20a-8501-400e-b336-d85724de5435"
response = requests.get(url)
response.raise_for_status()

# Lire le CSV avec le bon séparateur
df = pd.read_csv(io.StringIO(response.text), sep=',', low_memory=False)

# Vérifier que la colonne existe
if 'nom_enseigne' not in df.columns:
    raise ValueError(f"Colonne 'nom_enseigne' introuvable. Colonnes disponibles : {df.columns.tolist()}")

# Filtrer les lignes
filtered = df[df['nom_enseigne'] == 'MobiSDEC']

# Convertir en CSV
csv_buffer = io.StringIO()
filtered.to_csv(csv_buffer, index=False)
csv_data = csv_buffer.getvalue()

# Envoyer à Make via Webhook
webhook_url = "https://hook.eu2.make.com/y6lv95shd6wr1xomvm9im1qigy8f6ndi"
payload = {
    "filename": f"mobisdec_{datetime.today().strftime('%Y%m%d')}.csv",
    "file": csv_data
}
requests.post(webhook_url, json=payload)
