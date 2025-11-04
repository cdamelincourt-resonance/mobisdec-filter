name: Filter MobiSDEC CSV

on:
  workflow_dispatch:  # Permet à Zapier de déclencher manuellement

jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install pandas

      - name: Run script
        run: python filter_mobisdec.py
