# Data Collection Projects
### Web Scraping & API Monitoring — Python · Selenium · Folium · OpenData Paris

Deux projets de collecte et visualisation de données réelles :
scraping de médecins sur Doctolib et monitoring en temps réel des stations Vélib à Paris.

---

## Projets

### 1. Doctolib Scraping — `doctolib-scraping/`

Extraction automatisée de médecins sur Doctolib via Selenium avec gestion
de la pagination dynamique, anti-détection bot et export CSV.

**Pneumologues à Paris**
- 22 pages de résultats parcourues automatiquement
- ~470 médecins extraits (nom, spécialité, adresse, secteur)
- Export : `medecins_pneumologues_paris.csv`

**Pédiatres en Île-de-France**
- Scraping multi-villes sur toute l'Île-de-France
- Visualisation : histogramme du nombre de pédiatres par ville
- Export : `pediatres_idf.csv`

**Stack :** Python · Selenium · BeautifulSoup · Pandas · Matplotlib

---

### 2. Vélib Monitoring — `velib-monitoring/`

Système complet de monitoring des stations Vélib en temps réel
via l'API OpenData Paris.

**Modules :**

| Fichier | Description |
|---|---|
| `velib_api.py` | Appel API OpenData Paris — récupère toutes les stations en temps réel |
| `velib_carte.py` | Carte interactive Folium — stations colorées selon disponibilité |
| `velib_evolution.py` | Monitoring top 10 stations — collecte toutes les 2 min + graphique |
| `velib_surveillance.py` | Système d'alerte — détecte et surveille une station vide |

**Stack :** Python · Requests · Folium · Matplotlib · API REST

---

## Structure

```
data-collection-projects/
├── doctolib-scraping/
│   ├── pneumologues_paris.ipynb      # Scraper pneumologues Paris
│   ├── pediatres_idf.ipynb           # Scraper pédiatres Île-de-France
│   ├── medecins_pneumologues_paris.csv
│   ├── pediatres_idf.csv
│   └── histogramme_pediatres_idf.png
├── velib-monitoring/
│   ├── velib_api.py
│   ├── velib_carte.py
│   ├── velib_evolution.py
│   ├── velib_surveillance.py
│   └── velib_stations.csv
└── requirements.txt
```

---

## Installation

```bash
git clone https://github.com/meldub94/data-collection-projects.git
cd data-collection-projects
pip install -r requirements.txt
```

**Pour le scraping Doctolib :**
```bash
# Lancer le notebook
jupyter notebook doctolib-scraping/pneumologues_paris.ipynb
```

**Pour la carte Vélib :**
```bash
cd velib-monitoring
python velib_carte.py
# Ouvre velib_carte.html dans ton navigateur
```

**Pour le monitoring en temps réel :**
```bash
python velib_evolution.py
# Ctrl+C pour arrêter et afficher le graphique
```

---

## Aperçu

### Carte Vélib interactive
Chaque station est représentée par un cercle proportionnel à sa capacité.
- 🟢 Vert : vélos disponibles
- 🔴 Rouge : station vide

### Histogramme pédiatres Île-de-France
Répartition du nombre de pédiatres par ville en Île-de-France.

---

## Stack technique

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium)
![Folium](https://img.shields.io/badge/Folium-Maps-darkgreen)

`Python` · `Selenium` · `BeautifulSoup` · `Folium` · `Pandas`
`Matplotlib` · `Requests` · `API REST` · `OpenData Paris`

---

*Projets réalisés dans le cadre du MSc Data Management — Aivancity Paris-Cachan (2025-2026)*
