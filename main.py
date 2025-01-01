from epreuve_mathematiques import *
from fonctions_utiles import *
from epreuve_logiques import *
from epreuve_hasard import *
from epreuve_finale import *
from enigme_pere_fouras import *

def jeu():
    cle=0
    print(introduction())
    equipe=composer_equipe()
    while cle<3:
        for i in range(len(equipe)):
            cle+= equipe[i]["clé_gagner"]
        ch= menu_epreuves()
        player= choisir_joueur(equipe)
        if ch==1:
            epreuve=epreuve_math()
        if ch==2:
            epreuve=jeu_tictactoe()
        if ch==3:
            epreuve=epreuve_hasard()
        if ch==4:
            epreuve=enigme_pere_fouras()
        if epreuve==True:
            for i in range(len(equipe)):
                if player==equipe[i]:
                    equipe[i]["clé_gagner"]+=1
    print(salle_De_Tresor())
print(jeu())