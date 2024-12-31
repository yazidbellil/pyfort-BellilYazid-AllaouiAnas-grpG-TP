def introduction():
    print("Vous devez accomplir des épreuves pour gagner des clés et déverrouiller la salle du trésor.")
    print("L'objectif est de ramasser trois clés pour accéder à la salle du trésor.")

def composer_equipe():
    l=[]
    n=int(input("Combien de joueurs voulez vous ? "))
    clé_gagner=0
    r=0
    if n > 3:
        print("Impossible max 3")
        return composer_equipe()
    for i in range(n):
        equipe = {}
        nom=input("Nom du joueur "+str(i+1)+": ")
        equipe['nom']=nom
        profession=input("Profession du joueur "+str(i+1)+": ")
        equipe['profession']=profession
        leader=input("leader? Leader/Membre :")
        equipe['leader']=leader
        if leader=="Leader":
            r=r+1
        l.append(equipe)
    if r==0:
        l[0]['leader']="Leader"
    return l

def menu_epreuves():
    print('1. Épreuve de Mathématiques')
    print('2. Épreuve de Logique')
    print('3. Épreuve du hasard')
    print('4. Énigme du Père Fouras')
    print("Choix:")
    choix=int(input())
    return choix

def choisir_joueur(equipe):
    print("Choisissez un joueur :")
    for i in range(len(equipe)):
        print(str(i+1)+". "+equipe[i]['nom'],"("+equipe[i]['profession']+")", "Leader" if equipe[i]['leader']=="Leader" else "Membre")
    print("Entrez le numéro du joueur: ")
    num = int(input())
    return equipe[num-1]


