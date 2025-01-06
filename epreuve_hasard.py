##Fort Boyard Simulator ,Anas Allaoui , creation des epreuves de hasard

import random

# Fonction pour l'épreuve du Bonneteau
def bonneteau():
    """
    Fonction qui simule l'épreuve du Bonneteau.
    Rôle : Le joueur doit deviner sous quel bonneteau (A, B ou C) une clé est cachée.
    Résultat : Retourne True si le joueur trouve la clé, False sinon.
    """
    # Les trois bonneteaux possibles
    bonneteaux = ['A', 'B', 'C']
    essais = 2  # Nombre d'essais autorisés

     # Introduction à l'épreuve
    print("Bienvenue à l'épreuve du Bonneteau !")
    print("Une clé est cachée sous un des bonneteaux : A, B ou C.")
    print(f"Vous avez {essais} essais pour la trouver.\n")

    # Boucle pour chaque tentative
    for tentative in range(1, essais + 1):
        # Choisir un bonneteau aléatoire contenant la clé
        bonneteau_clé = random.choice(bonneteaux)
        print(f"Essai {tentative}/{essais}")

        # Demander au joueur de choisir un bonneteau
        choix = input("Choisissez un bonneteau (A, B ou C) : ").upper()

        # Vérification de la validité du choix
        if choix not in bonneteaux:
            print("Choix invalide. Essayez encore.")
            continue

        # Vérifier si le joueur a trouvé la clé
        if choix == bonneteau_clé:
            print("Bravo ! Vous avez trouvé la clé.")
            return True  # Succès

        # Sinon, informer le joueur que la clé n'est pas sous le bonneteau choisi
        else:
            print("Dommage, la clé n'est pas ici.")

    # Si le joueur n'a pas trouvé après tous les essais, afficher la solution
    print(f"Vous avez perdu. La clé était sous le bonneteau : {bonneteau_clé}")
    return False  # Échec


# Fonction pour l'épreuve du Lancer de dés
def jeu_lance_des():
    """
    Fonction qui simule l'épreuve du Lancer de dés.
    Rôle : Le joueur et le maître du jeu lancent deux dés. Le premier à obtenir un 6 gagne.
    Résultat : Retourne True si le joueur gagne, False si le maître gagne ou si aucun ne réussit.
    """
    essais_max = 3  # Nombre maximum d'essais

    # Introduction à l'épreuve
    print("Bienvenue à l'épreuve du Lancer de dés !")
    print("Le joueur et le maître du jeu lancent chacun deux dés.")
    print("Le premier à obtenir un 6 remporte la partie !\n")

    # Boucle pour chaque essai
    for essai in range(1, essais_max + 1):
        print(f"Essai {essai}/{essais_max}")

        # Lancer des dés pour le joueur
        input("Appuyez sur Entrée pour lancer vos dés...")
        joueur_dés = (random.randint(1, 6), random.randint(1, 6))
        print(f"Vos dés : {joueur_dés}")

        # Vérifier si le joueur a obtenu un 6
        if 6 in joueur_dés:
            print("Félicitations ! Vous avez obtenu un 6 et gagné la clé.")
            return True

        # Lancer des dés pour le maître du jeu
        maître_dés = (random.randint(1, 6), random.randint(1, 6))
        print(f"Dés du maître du jeu : {maître_dés}")

        # Vérifier si le maître du jeu a obtenu un 6
        if 6 in maître_dés:
            print("Le maître du jeu a obtenu un 6. Vous perdez.")
            return False

        # Si aucun 6 n'est obtenu, passer au prochain essai
        print("Aucun 6 obtenu. On passe au prochain essai.\n")

    # Si aucun joueur n'a obtenu un 6 après tous les essais
    print("Match nul ! Aucun 6 après trois essais.")
    return False


# Fonction pour choisir et exécuter une épreuve de hasard
def epreuve_hasard():
    """
    Fonction qui sélectionne et exécute aléatoirement une épreuve de hasard.
    Rôle : Choisir aléatoirement entre l'épreuve du Bonneteau et l'épreuve du Lancer de dés, puis l'exécuter.
    Résultat : Retourne le résultat de l'épreuve choisie (True si réussie, False sinon).
    """
    # Liste des épreuves disponibles
    epreuves = [bonneteau, jeu_lance_des]

    # Sélectionner une épreuve au hasard
    epreuve = random.choice(epreuves)

    # Exécuter l'épreuve sélectionnée
    return epreuve()
print(epreuve_hasard())