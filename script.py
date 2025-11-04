import os
import datetime
import csv
import requests
from io import StringIO

# URL du fichier source CSV
CSV_URL = "https://www.data.gouv.fr/fr/datasets/r/7a4e5e2e-0c3e-4a3c-8b4e-9f3a4c9f6f4b"

# URL du webhook Zapier
ZAPIER_WEBHOOK_URL = "https://hooks.zapier.com/hooks/catch/25244139/ustsv4r/"

def filter_mobisdec(csv_url: str) -> list[dict]:
    response = requests.get(csv_url)
    response.encoding = 'utf-8'
    if response.status_code != 200:
        raise Exception(f"Erreur lors du téléchargement : {response.status_code}")
    reader = csv.DictReader(StringIO(response.text))
    return [row for row in reader if row.get("nom_enseigne") == "MobiSDEC"]

def save_csv(data: list[dict], path: str):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def notify_zapier(filename: str, file_url: str):
    payload = {
        "filename": filename,
        "url": file_url
    }
    response = requests.post(ZAPIER_WEBHOOK_URL, json=payload)
    if response.status_code == 200:
        print("Webhook Zapier envoyé avec succès.")
    else:
        print(f"Erreur webhook Zapier : {response.status_code}")

def main():
    os.makedirs("output", exist_ok=True)
    today = datetime.date.today().strftime("%Y%m%d")
    filename = f"mobisdec_{today}.csv"
    filepath = os.path.join("output", filename)
    filtered_data = filter_mobisdec(CSV_URL)

    if filtered_data:
        save_csv(filtered_data, filepath)
        print(f"{len(filtered_data)} lignes écrites dans {filepath}")
        file_url = f"https://raw.githubusercontent.com/cdamelincourt-resonance/mobisdec-filter/main/output/{filename}"
        notify_zapier(filename, file_url)
    else:
        print("Aucune ligne trouvée avec nom_enseigne == 'MobiSDEC'")

if __name__ == "__main__":
    main()
