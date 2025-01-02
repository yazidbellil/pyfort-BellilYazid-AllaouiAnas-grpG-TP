##Fort Boyard Simulator, Anas Allaoui, creation de l'epreuve de logique

import random

# Fonction pour afficher le plateau de jeu
def afficher_plateau(plateau):
    """
    Affiche le plateau de jeu sous forme de grille.
    Rôle : Visualiser l'état actuel du plateau.
    Paramètres :
        - plateau : Liste 2D représentant le plateau du jeu.
    Retourne : Aucun, affiche uniquement le plateau.
    """
    for ligne in plateau:
        print(" | ".join(ligne))  # Affiche chaque ligne avec des séparateurs "|"
        print("-" * 5)  # Affiche une ligne de séparation entre les rangées


# Fonction pour vérifier si un joueur a gagné
def verifier_victoire(plateau, symbole):
    """
    Vérifie si un joueur (ou l'ordinateur) a gagné la partie.
    Rôle : Déterminer si un symbole (X ou O) a une ligne, une colonne ou une diagonale complète.
    Paramètres :
        - plateau : Liste 2D représentant le plateau du jeu.
        - symbole : Caractère ('X' ou 'O') représentant le joueur ou l'ordinateur.
    Retourne :
        - True si le joueur a gagné, False sinon.
    """
    # Vérifie les lignes
    for ligne in plateau:
        if all(case == symbole for case in ligne):  # Toutes les cases de la ligne doivent contenir le symbole
            return True

    # Vérifie les colonnes
    for col in range(3):
        if all(plateau[ligne][col] == symbole for ligne in range(3)):  # Toutes les cases de la colonne doivent contenir le symbole
            return True

    # Vérifie les diagonales
    if all(plateau[i][i] == symbole for i in range(3)) or all(plateau[i][2 - i] == symbole for i in range(3)):
        return True

    return False  # Si aucune des conditions n'est remplie, il n'y a pas de victoire


# Fonction principale pour le jeu du Morpion
def morpion():
    """
    Simule une partie de Morpion entre le joueur et l'ordinateur.
    Rôle : Permet au joueur de jouer contre l'ordinateur dans une épreuve pour gagner une clé.
    Résultat :
        - Retourne True si le joueur gagne, False sinon (en cas de victoire de l'ordinateur ou de match nul).
    """
    print("Bienvenue à l'épreuve du Morpion !")
    print("Affrontez l'ordinateur dans une partie de Morpion pour gagner la clé.\n")

    # Initialisation du plateau (3x3 vide)
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur_symbole = "X"  # Symbole du joueur
    ordinateur_symbole = "O"  # Symbole de l'ordinateur

    # Fonction interne pour trouver les cases disponibles
    def emplacement_disponible(plateau):
        """
        Trouve toutes les cases vides sur le plateau.
        Paramètres :
            - plateau : Liste 2D représentant le plateau du jeu.
        Retourne : Liste des tuples (ligne, colonne) représentant les cases disponibles.
        """
        return [(i, j) for i in range(3) for j in range(3) if plateau[i][j] == " "]

    # Boucle principale du jeu (maximum 9 tours)
    for tour in range(9):
        afficher_plateau(plateau)  # Affiche le plateau actuel

        if tour % 2 == 0:  # Tour du joueur
            print("C'est votre tour. Choisissez une case (ligne et colonne entre 0 et 2).")
            while True:
                try:
                    # Demande au joueur de choisir une case
                    ligne = int(input("Ligne : "))
                    colonne = int(input("Colonne : "))
                    # Vérifie si la case est disponible
                    if (ligne, colonne) in emplacement_disponible(plateau):
                        plateau[ligne][colonne] = joueur_symbole  # Place le symbole du joueur
                        break
                    else:
                        print("Case invalide ou déjà occupée. Réessayez.")
                except ValueError:
                    print("Veuillez entrer des nombres valides.")

            # Vérifie si le joueur a gagné
            if verifier_victoire(plateau, joueur_symbole):
                afficher_plateau(plateau)
                print("Bravo ! Vous avez gagné le Morpion et obtenu la clé !")
                return True

        else:  # Tour de l'ordinateur
            print("Tour de l'ordinateur...")
            # L'ordinateur choisit une case aléatoire disponible
            ligne, colonne = random.choice(emplacement_disponible(plateau))
            plateau[ligne][colonne] = ordinateur_symbole  # Place le symbole de l'ordinateur

            # Vérifie si l'ordinateur a gagné
            if verifier_victoire(plateau, ordinateur_symbole):
                afficher_plateau(plateau)
                print("L'ordinateur a gagné. Vous perdez cette épreuve.")
                return False

    # Si aucun joueur n'a gagné après 9 tours
    afficher_plateau(plateau)
    print("Match nul ! Personne ne gagne cette fois.")
    return False
