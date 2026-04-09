from velib_api import get_records  # importe la fonction qui interroge l'API Vélib
import matplotlib.pyplot as plt  # pour créer des graphiques
import time # pour gérer les pauses et l'heure

records = get_records()  # premier appel à l'API pour identifier les top 10

# trie toutes les stations par capacité décroissante et garde les 10 premières
top10 = sorted(records, key=lambda r: r['fields'].get('capacity', 0), reverse=True)[:10]

# dictionnaire pour retrouver facilement une station par son code
top10_names = {r['fields'].get('stationcode'): r['fields'].get('name') for r in top10}

# dictionnaire qui stockera les mesures au fil du temps
data = {name: [] for name in top10_names.values()}
timestamps = []  # liste des heures de chaque mesure

print("Collecte en cours... (Ctrl+C pour arrêter et afficher le graphique)")

try:
    while True:  # boucle infinie de collecte
        records = get_records()  # rafraîchit les données à chaque itération
        timestamps.append(time.strftime('%H:%M:%S'))  # enregistre l'heure de la mesure

        for record in records:
            fields = record['fields']
            if fields.get('stationcode') in top10_names:  # on ne garde que les top 10
                name = top10_names[fields['stationcode']]  # retrouve le nom depuis le code
                data[name].append(fields.get('numbikesavailable', 0))  # ajoute la mesure

        print(f"{timestamps[-1]} — données collectées")
        time.sleep(120)  # attend 2 minutes avant la prochaine collecte

except KeyboardInterrupt:  # déclenché quand tu fais Ctrl+C
    for name, bikes_counts in data.items():
        # trace une ligne par station avec des points à chaque mesure
        plt.plot(timestamps[:len(bikes_counts)], bikes_counts, marker='o', label=name)

    plt.title("Évolution des vélos disponibles - Top 10 stations")
    plt.xlabel("Heure")
    plt.ylabel("Vélos disponibles")
    plt.xticks(rotation=45)  # incline les heures pour éviter qu'elles se chevauchent
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # légende à droite du graphique
    plt.tight_layout()  # ajuste automatiquement les marges pour que tout rentre
    plt.show()  # affiche le graphique