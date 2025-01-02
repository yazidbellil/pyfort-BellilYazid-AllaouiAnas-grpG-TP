#Fort Boyard Simulator ,Yazid Bellil, creation des epreuves de mathematiques
import random
import math

# Fonction pour calculer la factorielle d'un nombre
def factorielle(a):
    """
    Calcule la factorielle d'un entier donné.
    Paramètres :
        - a : Entier positif.
    Retourne :
        - La factorielle de 'a'.
    """
    res = 1
    # Boucle pour multiplier tous les entiers de 1 à 'a'
    for i in range(1, a + 1):
        res = res * i
    return res


# Épreuve : Calculer la factorielle
def epreuves_math_factorielle():
    """
    Épreuve mathématique où le joueur doit calculer la factorielle d'un nombre aléatoire.
    Retourne :
        - True si la réponse est correcte, False sinon.
    """
    # Génère un nombre aléatoire entre 1 et 10
    a = random.randint(1, 10)
    while True:
        try:
            c = int(input(f"Veuillez calculer la factorielle de {a} : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
    b = factorielle(a)  # Calcule la factorielle correcte
    # Compare la réponse de l'utilisateur avec la réponse correcte
    if b == c:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Faux")
        return False


# Fonction pour générer une équation linéaire et la résoudre
def resoudre_equation_lineaire():
    """
    Génère une équation linéaire ax + b = 0 et calcule sa solution.
    Retourne :
        - a : Coefficient de x.
        - b : Terme constant.
        - x : Solution de l'équation.
    """
    # Génère les coefficients a et b aléatoires
    a, b = random.randint(1, 10), random.randint(1, 10)
    # Calcule la solution de l'équation
    x = -b / a
    return a, b, x


# Épreuve : Résolution d'une équation linéaire
def epreuve_math_equation():
    """
    Épreuve mathématique où le joueur doit résoudre une équation linéaire.
    Retourne :
        - True si la réponse est correcte, False sinon.
    """
    # Génère une équation et sa solution
    a, b, x = resoudre_equation_lineaire()
    print("Voici l'équation :", a, "x", "+", b, "= 0")
    while True:
        try:
            eq = float(input("Veuillez résoudre l'équation : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    if eq == x:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Faux")
        return False


 # Fonction pour vérifier si un nombre est premier
def est_premier(n):
    """
    Vérifie si un nombre est premier.
    Paramètres :
        - n : Entier.
    Retourne :
        - True si le nombre est premier, False sinon.
    """
    if n <= 1:  # Les nombres <= 1 ne sont pas premiers
        return False
    # Vérifie les divisibilités possibles jusqu'à √n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Fonction pour trouver le nombre premier le plus proche
def premier_plus_proche(n):
    """
    Trouve le nombre premier le plus proche d'un entier donné.
    Paramètres :
        - n : Entier.
    Retourne :
        - Le nombre premier le plus proche.
    """
    # Si le nombre lui-même est premier
    if est_premier(n):
        return n

    # Recherche du premier nombre premier inférieur
    inferieur = n - 1
    while inferieur > 1 and not est_premier(inferieur):
        inferieur -= 1

    # Recherche du premier nombre premier supérieur
    superieur = n + 1
    while not est_premier(superieur):
        superieur += 1

    # Retourne le plus proche (choisit le plus petit en cas d'égalité)
    if n - inferieur <= superieur - n:
        return inferieur
    else:
        return superieur


# Épreuve : Trouver le nombre premier le plus proche
def epreuve_math_premier():
    """
    Épreuve mathématique où le joueur doit trouver le nombre premier le plus proche d'un nombre donné.
    Retourne :
        - True si la réponse est correcte, False sinon.
    """
    n = random.randint(10, 20)  # Génère un nombre aléatoire entre 10 et 20
    # Demande à l'utilisateur de trouver le nombre premier le plus proche
    a = int(input(f"Trouve le nombre premier le plus proche de {n} : "))
    # Compare la réponse de l'utilisateur avec la solution correcte
    if a == premier_plus_proche(n):
        print("Correct! Vous gagnez une clé.")
        return True
    print("Faux")
    return False


# Épreuve : Roulette mathématique
def epreuve_roulette_mathematique():
    """
    Épreuve mathématique où le joueur doit effectuer une opération (addition, soustraction, multiplication) sur une série de nombres.
    Retourne :
        - True si la réponse est correcte, False sinon.
    """
    nb = []  # Liste pour stocker les nombres
    op = ['+', '-', '*']  # Liste des opérations possibles
    for i in range(5):  # Génère 5 nombres aléatoires
        nb.append(random.randint(1, 20))
    print(nb)  # Affiche les nombres pour l'épreuve
    res = nb[0]  # Initialisation avec le premier nombre
    p = random.choice(op)  # Choisit une opération aléatoire

    # Demande à l'utilisateur de faire l'opération et vérifie la réponse
    if p == '+':
        z = int(input("Faites l'addition des nombres : "))
        for i in range(1, 5):
            res = res + nb[i]
        if z == res:
            print("Correct! Vous gagnez une clé.")
            return True
    if p == '-':
        z = int(input("Faites la soustraction des nombres : "))
        for i in range(1, 5):
            res = res - nb[i]
        if z == res:
            print("Correct! Vous gagnez une clé.")
            return True
    if p == '*':
        z = int(input("Faites la multiplication des nombres : "))
        for i in range(1, 5):
            res = res * nb[i]
        if z == res:
            print("Correct! Vous gagnez une clé.")
            return True
    print("Faux")
    return False


# Fonction principale pour sélectionner une épreuve mathématique
def epreuve_math():
    """
    Sélectionne une épreuve mathématique aléatoire parmi plusieurs options.
    Retourne :
        - Résultat de l'épreuve (True ou False).
    """
    epreuves = [epreuves_math_factorielle, epreuve_math_equation, epreuve_math_premier, epreuve_roulette_mathematique]
    epreuve = random.choice(epreuves)  # Choisit une épreuve au hasard
    return epreuve()
