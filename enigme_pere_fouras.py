import json
import random

def charger_enigmes(fichier):
    with open(fichier, "r") as f:
        enigmes= json.load(f)
    return(enigmes)



def enigme_pere_fouras():
    # Variables locales
    nombre_essais = 3

    # Charger les énigmes depuis un fichier (simulé ici par une fonction)
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



