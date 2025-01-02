#Fort Boyard Simulator ,Yazid Bellil, creation des fonctions utiles au fichier main
# Fonction pour afficher une introduction au jeu
def introduction():
    """
    Fournit une introduction au jeu et explique l'objectif principal.
    Retourne :
        - Une chaîne de caractères avec l'introduction.
    """
    a = "Vous devez accomplir des épreuves pour gagner des clés et déverrouiller la salle du trésor."
    b = "L'objectif est de ramasser trois clés pour accéder à la salle du trésor."
    return a + "\n" + b


# Fonction pour composer l'équipe des joueurs
def composer_equipe():
    """
    Permet à l'utilisateur de créer une équipe de joueurs (maximum 3 joueurs).
    Retourne :
        - Une liste de dictionnaires contenant les informations des joueurs.
    """
    l = []  # Liste pour stocker les informations des joueurs
    while True:
        try:
            n = int(input("Combien de joueurs voulez-vous ? (max 3) "))
            if n > 3 or n < 1:
                print("Le nombre de joueurs doit être compris entre 1 et 3.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
    r = 0  # Compteur pour vérifier le nombre de leaders

    if n > 3:  # Limite maximale de 3 joueurs
        print("Impossible, maximum 3 joueurs.")
        return composer_equipe()  # Relance la fonction en cas de dépassement

    for i in range(n):
        equipe = {}  # Dictionnaire pour stocker les informations d'un joueur
        nom = input("Nom du joueur " + str(i + 1) + ": ")
        equipe['nom'] = nom  # Ajoute le nom du joueur
        profession = input("Profession du joueur " + str(i + 1) + ": ")
        equipe['profession'] = profession  # Ajoute la profession du joueur
        leader = input("Leader ? Leader/Membre : ")
        equipe['role'] = leader  # Définit le rôle du joueur (Leader ou Membre)
        equipe['clé_gagner'] = 0  # Initialise le nombre de clés gagnées à 0
        if leader == "Leader":
            r = r + 1  # Incrémente le compteur si le joueur est Leader
        l.append(equipe)

    # Si aucun leader n'est défini, le premier joueur devient automatiquement le leader
    if r == 0:
        l[0]['role'] = "Leader"

    return l


# Fonction pour afficher le menu des épreuves
def menu_epreuves():
    """
    Affiche un menu permettant de choisir une épreuve.
    Retourne :
        - Le choix de l'utilisateur sous forme d'entier.
    """
    while True:
        try:
            print('1. Épreuve de Mathématiques')
            print('2. Épreuve de Logique')
            print('3. Épreuve du Hasard')
            print('4. Énigme du Père Fouras')
            choix = int(input("Choix : "))
            if choix not in [1, 2, 3, 4]:
                print("Veuillez entrer un numéro entre 1 et 4.")
                continue
            return choix
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")


# Fonction pour choisir un joueur de l'équipe
def choisir_joueur(l):
    """
    Permet de choisir un joueur de l'équipe pour participer à une épreuve.
    Paramètres :
        - l : Liste des joueurs (chaque joueur est un dictionnaire).
    Retourne :
        - Le dictionnaire correspondant au joueur sélectionné.
    """
    while True:
        try:
            print("Choisissez un joueur :")
            for i in range(len(l)):
                role = "Leader" if l[i]['role'] == "Leader" else "Membre"
                print(f"{i + 1}. {l[i]['nom']} ({l[i]['profession']}) - {role}")
            num = int(input("Entrez le numéro du joueur : "))
            if num < 1 or num > len(l):
                print(f"Veuillez entrer un numéro entre 1 et {len(l)}.")
                continue
            return l[num - 1]
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")