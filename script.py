import pandas as pd
import requests
import yaml
import os

# Chemin vers le fichier YAML dans .github/workflows/
yaml_path = os.path.join(".github", "workflows", "filter.yml")

# Charger les paramètres
with open(yaml_path, "r") as f:
    config = yaml.safe_load(f)

# Télécharger le CSV
csv_url = config["csv_url"]
df = pd.read_csv(csv_url)

# Filtrer les données
filtered_df = df[df["nom_enseigne"] == config["filter"]["nom_enseigne"]]

# Convertir en dictionnaire
data = filtered_df.to_dict(orient="records")

# Envoyer à Zapier
webhook_url = config["zapier_webhook"]
response = requests.post(webhook_url, json={"data": data})

# Afficher le statut
print(f"Webhook status: {response.status_code}")
