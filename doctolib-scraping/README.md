# Doctolib Scraping
### Extraction automatisée de médecins via Selenium

Scraper Python qui parcourt Doctolib pour extraire les informations
des médecins avec gestion de la pagination dynamique et anti-détection bot.

---

## Projets

### Pneumologues à Paris
- **22 pages** parcourues automatiquement
- **~470 médecins** extraits : nom, spécialité, adresse, secteur
- Gestion cookies, pagination JS, anti-détection Selenium
- Export : `pneumologues_paris.csv`

### Pédiatres en Île-de-France
- Scraping multi-villes sur toute l'Île-de-France
- Visualisation : histogramme du nombre de pédiatres par ville
- Export : `pediatres_idf.csv`

---

## Fichiers

| Fichier | Description |
|---|---|
| `scraping_pneumologues_paris.ipynb` | Scraper pneumologues Paris — 22 pages |
| `scraping_pediatres_idf.ipynb` | Scraper pédiatres IDF + histogramme |
| `pneumologues_paris.csv` | Données extraites — pneumologues Paris |
| `pediatres_idf.csv` | Données extraites — pédiatres IDF |
| `histogramme_pediatres_idf.png` | Visualisation répartition par ville |

---

## Stack

`Python` · `Selenium` · `BeautifulSoup` · `Pandas` · `Matplotlib`

## Techniques

- Navigation automatisée Chrome via Selenium WebDriver
- Gestion des cookies et popups dynamiques
- Pagination automatique avec détection de fin de liste
- Anti-détection bot (user-agent personnalisé, masquage webdriver)
- Parsing HTML et export CSV via Pandas
