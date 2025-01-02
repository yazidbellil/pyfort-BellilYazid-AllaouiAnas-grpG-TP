def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 5)


def verifier_victoire(plateau, symbole):
    # Vérifie les lignes
    for ligne in plateau:
        if all(case == symbole for case in ligne):
            return True

    # Vérifie les colonnes
    for col in range(3):
        if all(plateau[ligne][col] == symbole for ligne in range(3)):
            return True

    # Vérifie les diagonales
    if all(plateau[i][i] == symbole for i in range(3)) or all(plateau[i][2 - i] == symbole for i in range(3)):
        return True

    return False


def morpion():
    print("Bienvenue à l'épreuve du Morpion !")
    print("Affrontez l'ordinateur dans une partie de Morpion pour gagner la clé.\n")

    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur_symbole = "X"
    ordinateur_symbole = "O"

    def emplacement_disponible(plateau):
        return [(i, j) for i in range(3) for j in range(3) if plateau[i][j] == " "]

    for tour in range(9):  # Maximum 9 tours
        afficher_plateau(plateau)

        if tour % 2 == 0:  # Tour du joueur
            print("C'est votre tour. Choisissez une case (ligne et colonne entre 0 et 2).")
            while True:
                try:
                    ligne = int(input("Ligne : "))
                    colonne = int(input("Colonne : "))
                    if (ligne, colonne) in emplacement_disponible(plateau):
                        plateau[ligne][colonne] = joueur_symbole
                        break
                    else:
                        print("Case invalide ou déjà occupée. Réessayez.")
                except ValueError:
                    print("Veuillez entrer des nombres valides.")

            if verifier_victoire(plateau, joueur_symbole):
                afficher_plateau(plateau)
                print("Bravo ! Vous avez gagné le Morpion et obtenu la clé !")
                return True

        else:  # Tour de l'ordinateur
            print("Tour de l'ordinateur...")
            ligne, colonne = random.choice(emplacement_disponible(plateau))
            plateau[ligne][colonne] = ordinateur_symbole

            if verifier_victoire(plateau, ordinateur_symbole):
                afficher_plateau(plateau)
                print("L'ordinateur a gagné. Vous perdez cette épreuve.")
                return False

    afficher_plateau(plateau)
    print("Match nul ! Personne ne gagne cette fois.")
    return False
