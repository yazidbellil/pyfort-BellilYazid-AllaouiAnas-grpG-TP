Fort Boyard Simulator

Présentation Générale

Titre du Projet

Le projet s’intitule Fort Boyard Simulator et vise à recréer des épreuves inspirées du célèbre jeu télévisé. Chaque joueur doit surmonter des défis variés pour décrocher les clés qui symbolisent sa réussite.

Contributeurs

Ce projet a été réalisé par Anas ALLAOUI et Yazid BELLIL.

Description

Le simulateur propose une expérience immersive, interactive et ludique. Les épreuves combinent des défis basés sur le hasard et la logique, où chaque partie est unique grâce à un système de sélection aléatoire. Le projet est conçu pour être modulable et facile à étendre.

Fonctionnalités Principales

1. Epreuves de hasard : Jouez au Bonneteau ou testez votre chance avec un lancer de dés.

2. Epreuves de logique : Affrontez un ordinateur dans une partie de Morpion stratégique.

3. Sélection aléatoire : Le programme choisit une épreuve aléatoire à chaque partie pour maintenir la diversité.

4. Feedback en direct : Le joueur est guidé par des messages clairs tout au long des épreuves.


Installation

Cloner le projet

Commencez par copier l’URL du dépôt GitHub, puis exécutez la commande suivante dans votre terminal :

////////////////////

Configurer un environnement Python

Pour isoler les dépendances, il est recommandé d’utiliser un environnement virtuel. Voici les étapes :

· Créez un environnement :

////////////////////////////////

Activez l’environnement :

· macOS/Linux :

//////////////////////////////////


Utilisation

Lancer une épreuve aléatoire

Le fichier main.py gère la sélection aléatoire des épreuves. Une fois lancé, le joueur est automatiquement redirigé vers un défi. Les instructions spécifiques sont affichées à l’écran pour guider le joueur.

Tester une épreuve spécifique

Si vous souhaitez tester une épreuve en particulier, vous pouvez exécuter directement le module correspondant :

· Bonneteau ou Lancer de dés :

· Morpion


Documentation Technique

Algorithme du Jeu

L'algorithme principal du jeu fonctionne en trois étapes simples :

1. Sélection aléatoire : Une épreuve est choisie parmi celles disponibles.

2. Participation : Le joueur suit les instructions et interagit avec l’épreuve.

3. Résultat : Le programme affiche si le joueur a réussi ou échoué.

Détails des Epreuves

Bonneteau

Le joueur doit deviner sous quel bonneteau (A, B ou C) se trouve la clé. La clé est placée de manière aléatoire à chaque partie. Le joueur a droit à deux tentatives.

Jeu de Lancer de Dés

Le joueur affronte le maître du jeu. Les deux lancent deux dés, et le premier à obtenir un 6 gagne. Le joueur dispose d’un maximum de trois tours pour réussir.

Morpion

Le joueur (symbole X) joue contre l’ordinateur (symbole O) sur un plateau 3x3. L’objectif est d’aligner trois symboles horizontalement, verticalement ou en diagonale. Si le plateau est rempli sans gagnant, le jeu se termine par un match nul.

Gestion des Erreurs

· Les entrées utilisateur sont vérifiées pour éviter les erreurs. Par exemple, dans le Morpion, les coordonnées doivent être comprises entre 0 et 2.

· Des messages d’erreur clairs sont affichés en cas d’entrée invalide, comme : "Choix invalide, veuillez réessayer."


Journal de Bord

Chronologie

· Semaine 1 : Conception des épreuves de hasard et de logique.

· Semaine 2 : Développement des fonctions principales (Morpion, Bonneteau, lancer de dés).

· Semaine 3 : Intégration des modules dans main.py et création du système de sélection aléatoire.

· Semaine 4 : Test du programme et rédaction de la documentation.

Répartition des Tâches

· : Création des épreuves et validation technique. ( exemple )

· : Intégration des modules, gestion du dépôt Git et documentation. ( exemple faut écris nos nom et prénom )


Tests et Validation

Stratégies de Test

1. Tests unitaires : Chaque fonction (ex. : morpion(), bonneteau()) a été testée séparément pour s’assurer de son bon fonctionnement.

2. Tests d’intégration : Tous les modules ont été testés ensemble via le fichier main.py.

3. Simulation utilisateur : Plusieurs parties complètes ont été simulées pour vérifier que les instructions sont claires et que les épreuves s’enchaînent correctement.

Résultats des Tests

· Les modules fonctionnent comme prévu, sans erreurs majeures.

· Les messages d’erreur apparaissent correctement lorsque des entrées invalides sont fournies.

· Les parties sont variées grâce à la sélection aléatoire.


Améliorations Possibles

· IA pour le Morpion : Ajouter une intelligence artificielle avancée pour rendre l’ordinateur plus compétitif.

· Nouvelles épreuves : Ajouter des épreuves comme des quiz ou des casse-têtes pour enrichir le contenu.

· Mode multijoueur : Permettre à deux joueurs de participer ensemble.

· Système de scores : Implémenter un tableau de scores pour suivre les performances des joueurs.