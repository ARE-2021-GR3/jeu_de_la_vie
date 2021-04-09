import matplotlib.pyplot as plt
import numpy as np
import random

#constantes
PROB_CONT = 0.2
PROB_DEATH = 0.1
NB_TURNS_TO_LIFE = 5 #on effectue 5 fois death(), puis on immunise notre cellule


matrice = np.array([[0, 1, 1, 1, 0],
                    [1, 0, 1, 0, 0], 
                    [0, 0, 2, 1, 0],
                    [0, 1, 1, 0, 1],
                    [1, 0, 1, 1, 0]])


# différents états possibles pour yne cellule :
# 0 - mort
# 1 - vivant
# 2 - contaminé
# 3 - immunisé


monde = np.random.randint(4, size=(6, 8))
print(monde)
print()

def voisinnage(monde, el): #matrice : List[List[int]], el : Tuple[int, int]
    """Préconditions : x>1 and y>1
    
    Renvoie une liste d'indices des éléments dans
    le voisinage de Moore de l'élément passé en paramètre
    """
    res = []
    
    
    x = np.shape(matrice)[0]
    y = np.shape(matrice)[1]
    
    xEl = el[0]
    yEl = el[1]
    
    #cas 1 (au milieu de la matrice)
    if ((xEl>0 and xEl<x-1) and (yEl>0 and yEl<y-1)):
        
        #ligne du haut
        for i in range(yEl-1, yEl+2):
            res.append((xEl-1, i))
            
        #à gauche et à droite
        res.append((xEl, yEl-1))
        res.append((xEl, yEl+1))
        
        #ligne du bas
        for i in range(yEl-1, yEl+2):
            res.append((xEl+1, i))
    
    #cas 2 (en haut à gauche)
    elif (xEl == 0 and yEl == 0):
        #à droite
        res.append((0, 1))
        #en bas
        res.append((1, 0))
        #en bas à droite
        res.append((1, 1))
    
    #cas 3 (en haut à droite)
    elif (xEl == 0 and yEl == y-1):
        #à gauche
        res.append((0, y-2))
        #en bas à gauche
        res.append((1, y-2))
        #en bas
        res.append((1, y-1))  
    
    #cas 4 (en bas à gauche)
    elif (xEl == x-1 and yEl == 0):
        #en haut
        res.append((x-2, 0))
        #en haut à droite
        res.append((x-2, 1))
        #à droite
        res.append((x-1, 1))
    
    #cas 5 (en bas à droite)
    elif (xEl == x-1 and yEl == y-1):
        #en haut à gauche
        res.append((x-2, y-2))
        #en haut
        res.append((x-2, y-1))
        #à gauche
        res.append((x-1, y-2))

    #cas 6 (bord haut)
    elif (xEl == 0):
        #à gauche
        res.append((0, yEl-1))
        #à droite
        res.append((0, yEl+1))
        #en bas
        for i in range(yEl-1, yEl+2):
            res.append((xEl+1, i))
        
    #cas 7 (bord gauche)
    elif (yEl == 0):
        #en haut
        res.append((xEl-1, 0))
        res.append((xEl-1, 1))
        #à droite
        res.append((xEl, 1))
        #en bas
        res.append((xEl+1, 0))
        res.append((xEl+1, 1))
    
    #cas 8 (bord droit)
    elif (yEl == y-1):
        #en haut
        res.append((xEl-1, y-2))
        res.append((xEl-1, y-1))
        #à gauche
        res.append((xEl, y-2))
        #en bas
        res.append((xEl+1, y-2))
        res.append((xEl+1, y-1))
    
    #cas 9 (bord bas)
    elif (xEl == x-1):
        #en haut
        for i in range(yEl-1, yEl+2):
            res.append((xEl-1, i))
        #à gauche
        res.append((x-1, yEl-1))
        #à droite
        res.append((x-1, yEl+1))
        
    return res

def contamination(monde, el, prob_cont):
    """Préconditions : el appartient à monde et monde[el] == 2; prob_cont >= 0.0 and prob_cont <= 1.0
    Contamine toutes les cellules en vie autour de notre el avec une proba de pron_cont
    """
    
    for i in voisinnage(monde, el):
        if (monde[i] == 1 and random.random()<=prob_cont):
            monde[i] = 2

    return monde

def death(monde, el, prob_death):
    """Préconditions : el appartient à monde et monde[el] == 2; prob_death >= 0.0 and prob_death <= 1.0
    Tue une cellule infectée avec une probabilité de prob_death"""
    if random.random()<=prob_death:
        monde[el] = 0
    
    return monde
    
    
#Jeu de tests
#cas 1
assert(voisinnage(matrice, (2, 2))) == [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)]
#cas 2
assert(voisinnage(matrice, (0, 0))) == [(0, 1), (1, 0), (1, 1)]
#cas 3
assert(voisinnage(matrice, (0, 4))) == [(0, 3), (1, 3), (1, 4)]
#cas 4
assert(voisinnage(matrice, (4, 0))) == [(3, 0), (3, 1), (4, 1)]
#cas 5
assert(voisinnage(matrice, (4, 4))) == [(3, 3), (3, 4), (4, 3)]
#cas 6
assert(voisinnage(matrice, (0, 2))) == [(0, 1), (0, 3), (1, 1), (1, 2), (1, 3)]
#cas 7
assert(voisinnage(matrice, (2, 0))) == [(1, 0), (1, 1), (2, 1), (3, 0), (3, 1)]
#cas 8
assert(voisinnage(matrice, (2, 4))) == [(1, 3), (1, 4), (2, 3), (3, 3), (3, 4)]
#cas 9
assert(voisinnage(matrice, (4, 2))) == [(3, 1), (3, 2), (3, 3), (4, 1), (4, 3)]

