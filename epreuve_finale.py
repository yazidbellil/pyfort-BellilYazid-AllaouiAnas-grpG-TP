import json
import random

def salle_de_tresor():
    # Charger les données du fichier JSON
    with open('data/indicesSalle.json', 'r', encoding= 'utf-8') as fichier:
        jeu_tv = json.load(fichier)

    # Sélectionner une année aléatoire
    annees = list(jeu_tv.keys())
    annee = random.choice(annees)

    # Sélectionner une émission aléatoire pour l'année choisie
    emissions = jeu_tv[annee]
    emission = random.choice(list(emissions.keys()))

    # Extraire les indices et le mot-code correspondant
    indices = emissions[emission]['Indices']
    mot_code = emissions[emission]['MOT-CODE']

    # Afficher les trois premiers indices
    print("Voici vos indices :")
    for indice in indices[:3]:
        print(f"- {indice}")

    # Initialiser les variables
    essais = 3
    reponse_correcte = False

    # Boucle principale du jeu
    while essais > 0:
        # Demander une réponse au joueur
        reponse = input("Entrez le mot-code : ").strip()

        if reponse == mot_code:
            reponse_correcte = True
            break
        else:
            essais -= 1
            if essais > 0:
                print(f"Incorrect ! Il vous reste {essais} essai(s).")
                if len(indices) > 3:
                    print(f"Indice supplémentaire : {indices[3]}\n")
            else:
                print("Désolé, vous avez épuisé tous vos essais.")
                print(f"Le mot-code correct était : {mot_code}")

    # Afficher le résultat final
    if reponse_correcte:
        print("Félicitations ! Vous avez trouvé le mot-code !")
    else:
        print("Dommage, vous avez perdu.")

# Appeler la fonction principale
    return salle_de_tresor()
print(salle_de_tresor())

