from velib_api import get_records  # importe la fonction get_records depuis velib_api.py
import time   # gérer les pauses entre les requêtes

# parcourt toutes les stations et retourne la première qui n'a aucun vélo disponible
def find_empty_station():
    records = get_records()  # récupère la liste des stations via velib_api.py
    for record in records:
        fields = record['fields']
        if fields.get('numbikesavailable', 0) == 0:  # si aucun vélo disponible
            return fields.get('stationcode'), fields.get('name')
    return None, None  # aucune station vide trouvée

# retourne le nombre de vélos disponibles pour la station identifiée par son code
def get_bikes_available(station_code):
    records = get_records()  # rafraîchit les données à chaque appel
    for record in records:
        fields = record['fields']
        if fields.get('stationcode') == station_code:  # on cherche la bonne station
            return fields.get('numbikesavailable', 0)
    return None  # station introuvable dans la réponse

station_code, station_name = find_empty_station()  # on cible une station vide au démarrage

if not station_code:
    print("Aucune station vide trouvée.")
else:
    print(f"Station surveillée : {station_name} (code {station_code})")
    print("Surveillance en cours... (Ctrl+C pour arrêter)\n")

    while True:  # boucle infinie jusqu'à ce qu'un vélo soit détecté
        bikes = get_bikes_available(station_code)  # interroge l'API pour cette station

        if bikes is None:
            print("Station introuvable dans la réponse.")
        elif bikes > 0:
            print(f"ALERTE : {bikes} vélos disponibles à la station {station_name} !")
            break  # on sort de la boucle dès qu'un vélo est disponible
        else:
            print(f"Toujours 0 vélo disponible à {station_name}. Prochaine vérification dans 2 minutes...")

        time.sleep(120)  # pause de 2 minutes avant la prochaine vérification