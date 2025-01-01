import random
import math

def factorielle(a):
    res=1
    for i in range(1,a+1):
        res=res*i
    return res

def epreuves_math_factorielle():
    a=random.randint(1,10)
    c=int(input(f"veuillez calculer la factorielle de {a}:"))
    b=factorielle(a)
    if b==c:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Faux")
        return False

def resoudre_equation_lineaire():
    a,b=random.randint(1,10),random.randint(1,10)
    x=-b/a
    return a,b,x

def epreuve_math_equation():
    a,b,x=resoudre_equation_lineaire()
    print("voici l'equation :",a,"x","+",b)
    eq=float(input("veuillez resoudre l'equation :"))
    if eq==x:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Faux")
        return False

def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def premier_plus_proche(n):
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

        # Retourne le plus proche (privilégie le plus petit en cas d'égalité)
        if n - inferieur <= superieur - n:
            return inferieur
        else:
            return superieur

def epreuve_math_premier():
    n=random.randint(10,20)
    a = int(input(f"trouve le premier le plus proche de {n}:"))
    if a==premier_plus_proche(n):
        print("Correct! Vous gagnez une clé.")
        return True
    print("Faux")
    return False

def epreuve_roulette_mathematique():
    nb=[]
    op=['+','-','*']
    for i in range(5):
        nb.append(random.randint(1,20))
    print(nb)
    res=nb[0]
    p=random.choice(op)
    if p=='+':
        z=int(input("fait laddition des nombres"))
        for i in range(1,5):
            res=res+nb[i]
        if z==res:
            print("Correct! Vous gagnez une clé.")
            return True
    if p=='-':
        z = int(input("fait la soustraction des nombres"))
        for i in range(1,5):
            res=res-nb[i]
        if z==res:
            print("Correct! Vous gagnez une clé.")
            return True
    if p=='*':
        z = int(input("fait la multiplication des nombres"))
        for i in range(1,5):
            res=res*nb[i]
        if z==res:
            print("Correct! Vous gagnez une clé.")
            return True
    print("Faux")
    return False

def epreuve_math():
    epreuves=[epreuves_math_factorielle,epreuve_math_equation,epreuve_math_premier,epreuve_roulette_mathematique]
    epreuve=random.choice(epreuves)
    return epreuve()













