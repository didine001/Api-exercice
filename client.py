import requests

FAST_API_URL = "http://127.0.0.1:8000"


def get_artists_by_name(artist_name):
    response = requests.get(
        f"{FAST_API_URL}/artists/{artist_name}"
    )  # we use the endpoint created in api.py and we use the corresponding route to get the data.
    return (
        response.json()
    )  # We format on json because if we don't it returns an object.


def read_genres():
    response = requests.get(f"{FAST_API_URL}/genres/")
    return response.json()


def get_albums_by_artist_id(artist_id):
    response = requests.get(f"{FAST_API_URL}/albums/{artist_id}")
    return response.json()


def get_track_name_by_album_id(album_id):
    response = requests.get(f"{FAST_API_URL}/tracks/{album_id}")
    return response.json()


def delete_artist(artist_id):
    response = requests.delete(f"{FAST_API_URL}/artists/{artist_id}")
    return response.json()


def update_artist_name(artist_id, name):
    response = requests.put(f"{FAST_API_URL}/artists/{artist_id}?name={name}")
    return response.json()


def create_artist(name):
    response = requests.post(f"{FAST_API_URL}/artists/?new_name={name}")
    return response.json()


choix = (
    "1 Rechercher des artistes par nom\n"
    "2 Lire les genres\n"
    "3 Obtenir des albums par ID d'artiste\n"
    "4 Obtenir des noms de pistes par ID d'album\n"
    "5 Supprimer un artiste\n"
    "6 Mettre à jour le nom d'un artiste\n"
    "7 Créer un artiste\n"
    "q Quitter\n"
    "Entrez le numéro : "
)

while True:
    user_choice = input(choix)

    if user_choice == "q":
        break  # Sortir de la boucle puisqu'on veut quitter

    match user_choice:
        case "1":
            artist_name = input("Entrez le nom de l'artiste : ")
            result = get_artists_by_name(artist_name)
            print(result)

        case "2":
            result = read_genres()
            print(result)

        case "3":
            artist_id = input("Entrez l'ID de l'artiste : ")
            result = get_albums_by_artist_id(artist_id)
            print(result)

        case "4":
            album_id = input("Entrez l'ID de l'album : ")
            result = get_track_name_by_album_id(album_id)
            print(result)

        case "5":
            artist_id = input("Entrez l'ID de l'artiste : ")
            result = delete_artist(artist_id)

        case "6":
            artist_id = input("Entrez l'ID de l'artiste : ")
            name = input("Entrez le nouveau nom de l'artiste : ")
            result = update_artist_name(artist_id, name)

        case "7":
            name = input("Entrez le nom de l'artiste : ")
            result = create_artist(name)

        case _:
            print("Option invalide. Veuillez choisir une option valide.")
