##Fort Boyard Simulator ,Yazid Bellil, creation du jeu
# Importation des modules nécessaires pour les différentes épreuves et fonctions
from epreuve_mathematiques import *  # Module pour les épreuves mathématiques
from fonctions_utiles import *  # Module contenant des fonctions générales
from epreuve_logiques import *  # Module pour les épreuves logiques
from epreuve_hasard import *  # Module pour les épreuves de hasard
from epreuve_finale import *  # Module pour la salle du trésor
from enigme_pere_fouras import *  # Module pour les énigmes du Père Fouras

# Fonction principale pour le déroulement du jeu
def jeu():
    """
    Cette fonction est le cœur du jeu. Elle gère :
    - L'introduction.
    - La composition de l'équipe.
    - La boucle des épreuves pour obtenir 3 clés.
    - L'accès à la salle du trésor.
    """
    cle = 0  # Compteur pour les clés obtenues
    print(introduction())  # Affichage de l'introduction
    equipe = composer_equipe()  # Création de l'équipe

    # Boucle principale du jeu pour gagner 3 clés
    while cle < 3:
        ch = menu_epreuves()  # Affichage du menu des épreuves et choix de l'épreuve
        player = choisir_joueur(equipe)  # Sélection du joueur pour l'épreuve

        # Exécution de l'épreuve choisie
        if ch == 1:
            epreuve = epreuve_math()  # Épreuve de mathématiques
        elif ch == 2:
            epreuve = morpion()  # Épreuve de logique (Morpion)
        elif ch == 3:
            epreuve = epreuve_hasard()  # Épreuve de hasard
        elif ch == 4:
            epreuve = enigme_pere_fouras()  # Énigme du Père Fouras

         # Si l'épreuve est réussie, le joueur gagne une clé
        if epreuve == True:
            for i in range(len(equipe)):
                if player == equipe[i]:  # Trouver le joueur correspondant dans l'équipe
                    equipe[i]["clé_gagner"] += 1  # Incrémenter le compteur de clés du joueur
            cle += 1  # Incrémenter le compteur total de clés

    # Une fois 3 clés obtenues, accéder à la salle du trésor
    print(salle_De_Tresor())

# Lancer le jeu
print(jeu())
