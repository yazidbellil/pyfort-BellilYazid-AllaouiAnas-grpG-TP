#Fort Boyard Simulator ,Yazid Bellil, permet d'acceder a la salle au tresor

import json
import random

# Charger les données depuis un fichier JSON
def charger_donnees(fichier):
    """
    Fonction pour charger des données depuis un fichier JSON.

    Rôle :
    - Cette fonction lit un fichier JSON contenant des données nécessaires pour la salle du trésor.
    - Elle gère les exceptions si le fichier est introuvable ou si son contenu est invalide.

    Paramètre :
    - fichier (str) : Le chemin du fichier JSON à lire.

    Résultat retourné :
    - dict : Le contenu du fichier JSON sous forme de dictionnaire si le fichier est valide.
    - None : Si le fichier est introuvable ou si le JSON est invalide, la fonction retourne `None`.
    """
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erreur : fichier introuvable.")
        return None
    except json.JSONDecodeError:
        print("Erreur : format JSON invalide.")
        return None


# Fonction principale pour la salle du trésor
def salle_De_Tresor():
    """
    Fonction qui simule l'épreuve de la salle du trésor de Fort Boyard.

    Rôle :
    - Sélectionner aléatoirement une année et une émission dans les données fournies.
    - Afficher des indices et permettre au joueur de deviner le mot-code dans un nombre limité d'essais.
    - Ajouter des indices supplémentaires si le joueur échoue dans ses tentatives initiales.

    Paramètres :
    - Aucun paramètre explicite n'est attendu. La fonction dépend du fichier JSON "Data/indicesSalle.json".

    Résultat retourné :
    - Aucun retour explicite (fonction basée sur les interactions utilisateur).
    - Affiche un message indiquant si le joueur a réussi ou échoué.

    Exceptions gérées :
    - Si le fichier JSON est introuvable ou invalide, la fonction affiche un message d'erreur et s'arrête.
    """
    # Charger les données du fichier
    fichier = "Data/indicesSalle.json"  # Nom du fichier JSON
    donnees = charger_donnees(fichier)
    if donnees is None:
        return

    # Sélectionner une année et une émission aléatoirement
    annees = list(donnees["Fort Boyard"].keys())
    annee = random.choice(annees)
    emissions = list(donnees["Fort Boyard"][annee].keys())
    emission = random.choice(emissions)

     # Extraire les indices et le mot-code
    indices = donnees["Fort Boyard"][annee][emission]["Indices"]
    mot_code = donnees["Fort Boyard"][annee][emission]["MOT-CODE"]

    print("\nBienvenue dans la salle du trésor !")
    print("Voici les trois premiers indices :")
    for indice in indices[:3]:
        print(f"- {indice}")

    essais_restants = 3
    reussi = False

    # Boucle des essais
    while essais_restants > 0:
        reponse = input("\nEntrez votre mot-code : ").strip().upper()
        if reponse == mot_code:
            reussi = True
            break
        else:
            essais_restants -= 1
            if essais_restants > 0:
                print(f"Mauvaise réponse. Indice supplémentaire : {indices[3 + essais_restants]}")
                print(f"Essais restants : {essais_restants}")
            else:
                print("Mauvaise réponse. Vous n'avez plus d'essais.")

    # Résultat final
    if reussi:
        print("\nFélicitations ! Vous avez trouvé le mot-code et accédé au trésor !")
    else:
        print(f"\nVous avez échoué. Le mot-code correct était : {mot_code}")
