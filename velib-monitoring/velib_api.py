import requests  # pour faire des requêtes HTTP

# URL de l'API Vélib
url = "https://data.opendatasoft.com/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel%40parisdata&facet=overflowactivation&facet=creditcard&facet=kioskstate&facet=station_state"

start = 0  # premier enregistrement
rows = 2000 # nb max d'enregistrements
params = {'start': start, 'rows': rows}  # paramètres ajoutés à l'URL de la requête

# envoie une requête GET à l'API et retourne la liste des stations sous forme de dictionnaires
def get_records():
    return requests.get(url, params=params).json()['records']