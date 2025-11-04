import pandas as pd
import requests
import io
from datetime import datetime

# Télécharger le fichier CSV
url = "https://www.data.gouv.fr/api/1/datasets/r/eb76d20a-8501-400e-b336-d85724de5435"
response = requests.get(url)
response.raise_for_status()

# Lire le CSV
df = pd.read_csv(io.StringIO(response.text), sep=';', low_memory=False)

# Filtrer
filtered = df[df['nom_enseigne'] == 'MobiSDEC']

# Convertir en CSV
csv_buffer = io.StringIO()
filtered.to_csv(csv_buffer, index=False)
csv_data = csv_buffer.getvalue()

# Envoyer à Make via Webhook
webhook_url = "https://hook.make.com/TON_WEBHOOK_ID_ICI"
payload = {
    "filename": f"mobisdec_{datetime.today().strftime('%Y%m%d')}.csv",
    "file": csv_data
}
requests.post(webhook_url, json=payload)
