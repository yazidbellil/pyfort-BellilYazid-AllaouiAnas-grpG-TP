import json
import random

# Charger les données depuis un fichier JSON
def charger_donnees(fichier):
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

# Appel de la fonction
print(salle_De_Tresor())
