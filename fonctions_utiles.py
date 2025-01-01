def introduction():
    a="Vous devez accomplir des épreuves pour gagner des clés et déverrouiller la salle du trésor."
    b="L'objectif est de ramasser trois clés pour accéder à la salle du trésor."
    return a+"\n"+b
def composer_equipe():
    global l
    l=[]
    n=int(input("Combien de joueurs voulez vous ? "))
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
        equipe['role']=leader
        equipe['clé_gagner']=0
        if leader=="Leader":
            r=r+1
        l.append(equipe)
    if r==0:
        l[0]['role']="Leader"
    return l

def menu_epreuves():
    print('1. Épreuve de Mathématiques')
    print('2. Épreuve de Logique')
    print('3. Épreuve du hasard')
    print('4. Énigme du Père Fouras')
    print("Choix:")
    choix=int(input())
    return choix

def choisir_joueur(l):
    print("Choisissez un joueur :")
    for i in range(len(l)):
        print(str(i+1)+". "+l[i]['nom'],"("+l[i]['profession']+")", "Leader" if l[i]['role']=="Leader" else "Membre")
    print("Entrez le numéro du joueur: ")
    num = int(input())
    return l[num-1]



