# AlgoInvest&Trade

Objectif : stratégies d'investissement pour engranger le maximum de bénéfices.

Livrables :
1) Fichier Python `bruteforce.py` avec la solution de force brute. 
2) Fichier Python `optimized.py` avec la version optimisée de l'algorithme.
3) Jeu de diapositives au format PDF


## Variables 
Au début de chacun de ces scripts, on peut choisir de changer :
- Le nom du fichier csv qui va être pour les inputs (par defaut = csv/20actions.csv")
- La capacité maximum de l'investissement (par défaut = 500)


## Brute de force
On utilise l'outil combinations du module itertools pour générer toutes les combinaisons possibles.

Pour lancer le script, il faut écrire dans le terminal :
```
python bruteforce.py 
```


## Version optimisée
On utilise l'algo Knapsack 0/1 en tabulation pour trouver la solution optimal

Pour lancer le script, il faut écrire dans le terminal :
```
python optimized.py
```

Les différentes étapes :
### 1) Nettoyage des datas
### 2) Manipulation des datas pour éviter d'avoir des virgules flottantes dans les prix
### 3) Ensuite on utilise l'algorithme 0/1 knapsack permettant de trouver la meilleure combinaison possible.
### 4) Dernière manipulation avant d'imprimer le résultat



