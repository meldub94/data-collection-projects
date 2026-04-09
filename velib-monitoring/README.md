
# Vélib Monitoring
### Monitoring temps réel des stations Vélib via API OpenData Paris

Système complet de collecte, visualisation et surveillance
des stations Vélib en temps réel via l'API publique OpenData Paris.

---

## Modules

| Fichier | Description |
|---|---|
| `velib_api.py` | Appel API OpenData Paris — récupère toutes les stations |
| `velib_carte.py` | Carte interactive Folium — stations colorées selon disponibilité |
| `velib_evolution.py` | Monitoring top 10 stations — collecte toutes les 2 min + graphique |
| `velib_surveillance.py` | Système d'alerte — surveille une station vide jusqu'au retour d'un vélo |
| `velib_stations.csv` | Données stations extraites |

---

## Utilisation

```bash
# Carte interactive
python velib_carte.py
# → génère velib_carte.html à ouvrir dans le navigateur

# Monitoring en temps réel (top 10 stations)
python velib_evolution.py
# → collecte toutes les 2 min, Ctrl+C pour afficher le graphique

# Surveillance d'une station vide
python velib_surveillance.py
# → alerte dès qu'un vélo devient disponible
```

---

## Carte interactive

Chaque station est représentée par un cercle proportionnel à sa capacité :
- **Vert** : vélos disponibles
- **Rouge** : station vide

Clic sur un cercle → nom de la station, vélos disponibles, capacité totale.

---

## Stack

`Python` · `Requests` · `Folium` · `Matplotlib` · `API REST` · `OpenData Paris`

## Source des données

API Vélib Métropole — OpenData Paris (temps réel)
`https://data.opendatasoft.com` — mise à jour toutes les 2 minutes
