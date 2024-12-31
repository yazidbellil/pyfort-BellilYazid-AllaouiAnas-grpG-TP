import random
def bonneteau():
    bonneteaux = ['A', 'B', 'C']
    essais = 2
    print("Bienvenue à l'épreuve du Bonneteau !")
    print("Une clé est cachée sous un des bonneteaux : A, B ou C.")
    print(f"Vous avez {essais} essais pour la trouver.\n")
    for tentative in range(1, essais + 1):
        bonneteau_clé = random.choice(bonneteaux)
        print(f"Essai {tentative}/{essais}")
        choix = input("Choisissez un bonneteau (A, B ou C) : ").upper()
        if choix not in bonneteaux:
            print("Choix invalide. Essayez encore.")
            continue
        if choix == bonneteau_clé:
            print("Bravo ! Vous avez trouvé la clé.")
            return True
        else:
            print("Dommage, la clé n'est pas ici.")
    print(f"Vous avez perdu. La clé était sous le bonneteau : {bonneteau_clé}")
    return False
def jeu_lance_des():
    essais_max = 3
    print("Bienvenue à l'épreuve du Lancer de dés !")
    print("Le joueur et le maître du jeu lancent chacun deux dés.")
    print("Le premier à obtenir un 6 remporte la partie !\n")
    for essai in range(1, essais_max + 1):
        print(f"Essai {essai}/{essais_max}")
        input("Appuyez sur Entrée pour lancer vos dés...")
        joueur_dés = (random.randint(1, 6), random.randint(1, 6))
        print(f"Vos dés : {joueur_dés}")
        if 6 in joueur_dés:
            print("Félicitations ! Vous avez obtenu un 6 et gagné la clé.")
            return True
        maître_dés = (random.randint(1, 6), random.randint(1, 6))
        print(f"Dés du maître du jeu : {maître_dés}")
        if 6 in maître_dés:
            print("Le maître du jeu a obtenu un 6. Vous perdez.")
            return False
        print("Aucun 6 obtenu. On passe au prochain essai.\n")
    print("Match nul ! Aucun 6 après trois essais.")
    return False
def epreuve_hasard():
    epreuves = [bonneteau, jeu_lance_des]
    epreuve = random.choice(epreuves)
    return epreuve()

