#Fort Boyard Simulator, Yazid Bellil, creation de l'enigme pere fouras
import json
import random


def charger_enigmes(fichier):
    """
    Fonction pour charger une liste d'énigmes depuis un fichier JSON.

    Rôle : Cette fonction lit un fichier JSON contenant des énigmes et retourne les données sous forme de liste de dictionnaires.

    Paramètre :
    - fichier (str) : Le chemin du fichier JSON contenant les énigmes.

    Résultat retourné :
    - enigmes (list) : Une liste de dictionnaires, chaque dictionnaire contenant une question et sa réponse associée.
    """
    with open(fichier, "r") as f:
        enigmes = json.load(f)
    return enigmes


def enigme_pere_fouras():
    """
    Fonction qui gère une interaction avec une énigme du Père Fouras.

    Rôle :
    - Sélectionner une énigme aléatoire depuis un fichier JSON.
    - Afficher l'énigme et permettre au joueur de tenter de répondre.
    - Gérer un nombre limité d'essais pour résoudre l'énigme.
    - Retourner si l'énigme a été résolue ou non.

    Paramètres :
    - Aucun paramètre explicite n'est attendu, mais la fonction dépend du fichier "data/enigmesPF.json".

    Résultat retourné :
    - bool :
        - `True` si le joueur répond correctement à l'énigme dans les 3 essais.
        - `False` si le joueur échoue après les 3 essais.
    """
    # Variables locales
    nombre_essais = 3

    # Charger les énigmes depuis un fichier JSON
    enigmes = charger_enigmes("data/enigmesPF.json")

    # Choisir une énigme aléatoire
    enigme = random.choice(enigmes)

    # Afficher la question
    print("Voici votre énigme :")
    print(enigme["question"])

    # Boucle pour les essais
    while nombre_essais > 0:
    # Demander la réponse au joueur
        reponse = input("Votre réponse : ").strip().lower()

        # Vérifier si la réponse est correcte
        if reponse == enigme["reponse"]:
            print("Bravo ! La réponse est correcte. Vous gagnez la clé !")
            return True
        else:
            # Réduire le nombre d'essais
            nombre_essais -= 1
            if nombre_essais > 0:
                print(f"Mauvaise réponse. Il vous reste {nombre_essais} essai(s).")
            else:
                print("Vous avez échoué à l'énigme.")
                print(f"La bonne réponse était : {enigme['reponse']}.")
                return False
