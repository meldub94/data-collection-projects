from velib_api import get_records  # importe la fonction qui interroge l'API Vélib
import folium  # pour créer des cartes interactives

records = get_records()  # récupère toutes les stations

# crée une carte centrée sur Paris avec un niveau de zoom initial
carte = folium.Map(location=[48.8566, 2.3522], zoom_start=13)

for record in records:
    fields = record['fields']
    coords = fields.get('coordonnees_geo') # coordonnées de la station
    name = fields.get('name', 'Inconnue')# nom de la station
    capacity = fields.get('capacity', 0)  # nombre total de places
    bikes = fields.get('numbikesavailable', 0)   # nombre de vélos disponibles

    if coords:  # certaines stations n'ont pas de coordonnées, on les ignore
        folium.CircleMarker(
            location=coords,
            radius=capacity / 5,  # taille proportionnelle à la capacité
            color='green' if bikes > 0 else 'red', # vert = vélos dispo, rouge = vide
            fill=True,
            popup=f"{name} — {bikes} vélos / {capacity} places"  # info au clic sur le cercle
        ).add_to(carte)

carte.save('velib_carte.html')  # sauvegarde la carte dans un fichier HTML
print("Carte sauvegardée dans velib_carte.html")