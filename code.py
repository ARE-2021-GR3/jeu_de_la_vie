import matplotlib.pyplot as plt
import numpy as np
import random
import time

#constantes
PROB_CONT = 0.2
PROB_DEATH = 0.02
NB_TURNS_TO_LIFE = 5 #nombre de tours infectés avant d'être immunisé (non ajouté au code)
TAILLE_MONDE = (100, 100) #tuple qui donne la taille de notre monde


matrice = np.array([[0, 1, 1, 1, 0],
                    [1, 0, 1, 0, 0], 
                    [0, 0, 2, 1, 0],
                    [0, 1, 1, 0, 1],
                    [1, 0, 1, 1, 0]])



# differents etats possibles pour une cellule
# 0 - mort
# 1 - vivant
# 2 - contamine
# 3 - immunise

np.random.seed(19680801)


def creation_monde(taille):
    monde = np.random.randint(4, size=(taille[0], taille[1]))
    return monde

monde = creation_monde(TAILLE_MONDE)
print(monde)
print()

def voisinnage(monde, el): #matrice : List[List[int]], el : Tuple[int, int]
    """Preconditions : x>1 and y>1
    
    Renvoie une liste d'indices des elements dans
    le voisinage de Moore de l'element passe en parametre
    """
    res = []
    
    
    x = np.shape(monde)[0]
    y = np.shape(monde)[1]
    
    xEl = el[0]
    yEl = el[1]
    
    #cas 1 (au milieu de la matrice)
    if ((xEl>0 and xEl<x-1) and (yEl>0 and yEl<y-1)):
        
        #ligne du haut
        for i in range(yEl-1, yEl+2):
            res.append((xEl-1, i))
            
        #a gauche et a droite
        res.append((xEl, yEl-1))
        res.append((xEl, yEl+1))
        
        #ligne du bas
        for i in range(yEl-1, yEl+2):
            res.append((xEl+1, i))
    
    #cas 2 (en haut a gauche)
    elif (xEl == 0 and yEl == 0):
        #a droite
        res.append((0, 1))
        #en bas
        res.append((1, 0))
        #en bas a droite
        res.append((1, 1))
    
    #cas 3 (en haut a droite)
    elif (xEl == 0 and yEl == y-1):
        #a gauche
        res.append((0, y-2))
        #en bas a gauche
        res.append((1, y-2))
        #en bas
        res.append((1, y-1))  
    
    #cas 4 (en bas a gauche)
    elif (xEl == x-1 and yEl == 0):
        #en haut
        res.append((x-2, 0))
        #en haut a droite
        res.append((x-2, 1))
        #a droite
        res.append((x-1, 1))
    
    #cas 5 (en bas a droite)
    elif (xEl == x-1 and yEl == y-1):
        #en haut a gauche
        res.append((x-2, y-2))
        #en haut
        res.append((x-2, y-1))
        #a gauche
        res.append((x-1, y-2))

    #cas 6 (bord haut)
    elif (xEl == 0):
        #a gauche
        res.append((0, yEl-1))
        #a droite
        res.append((0, yEl+1))
        #en bas
        for i in range(yEl-1, yEl+2):
            res.append((xEl+1, i))
        
    #cas 7 (bord gauche)
    elif (yEl == 0):
        #en haut
        res.append((xEl-1, 0))
        res.append((xEl-1, 1))
        #a droite
        res.append((xEl, 1))
        #en bas
        res.append((xEl+1, 0))
        res.append((xEl+1, 1))
    
    #cas 8 (bord droit)
    elif (yEl == y-1):
        #en haut
        res.append((xEl-1, y-2))
        res.append((xEl-1, y-1))
        #a gauche
        res.append((xEl, y-2))
        #en bas
        res.append((xEl+1, y-2))
        res.append((xEl+1, y-1))
    
    #cas 9 (bord bas)
    elif (xEl == x-1):
        #en haut
        for i in range(yEl-1, yEl+2):
            res.append((xEl-1, i))
        #a gauche
        res.append((x-1, yEl-1))
        #a droite
        res.append((x-1, yEl+1))
        
    return res

def contamination(monde, el, prob_cont):
    """Preconditions : el appartient a monde et monde[el] == 2; prob_cont >= 0.0 and prob_cont <= 1.0
    Renvoie la liste des cellules contaminées par notre cellule el
    """
    
    liste_cont = []
    
    
    for i in voisinnage(monde, el):
        if random.random()<=prob_cont:
            liste_cont.append(i)

    return liste_cont

def death(monde, el, prob_death):
    """Preconditions : el appartient a monde et monde[el] == 2; prob_death >= 0.0 and prob_death <= 1.0
    Tue une cellule infectee avec une probabilite de prob_death"""
    if random.random()<=prob_death:
        return 1
    else:
        return 0
    
def tour(monde):

    x = np.shape(monde)[0]
    y = np.shape(monde)[1]
    
    monde_update = np.zeros((x,y), dtype = int)
    
    
    # premier parcours pour placer les cellules mortes/immunisées
    for i in range(x):
        for j in range(y):
            if monde[i][j] == 3:
                monde_update[i][j] = 3
                
    # deuxième parcours pour placer les cellules contaminées
    for i in range(x):
        for j in range(y):
            if monde[i][j] == 2:
                for k in contamination(monde, (i, j), PROB_CONT):
                    if monde[k] == 1:
                        monde_update[k] = 2

                if death(monde, (i, j), PROB_DEATH):
                  monde_update[i][j] = 0
                else :
                  monde_update[i][j] = 2
    
    # troisième parcours pour placer les cellules vivantes
    for i in range(x):
        for j in range(y):
            if (monde[i][j] == 1 and monde_update[i][j] == 0):
                monde_update[i][j] = 1
    
    return monde_update



max_tour = 20
for i in range(1, max_tour + 1):
    plt.matshow(monde)
    monde = tour(monde)
    plt.title(i)
  
    print("Tour", i)
    plt.pause(0.05)
    if (i==1 or i==max-1):
      mort = 0
      vivant = 0
      contamine = 0
      immunise = 0
      x = np.shape(monde)[0]
      y = np.shape(monde)[1]
      for j in range (x):
        for k in range (y):
          if (monde[j][k]==0):
            mort+=1
          if (monde[j][k]==1):
            vivant+=1
          if (monde[j][k]==2):
            contamine+=1
          if (monde[j][k]==3):
            immunise+=1
      print(f"Mort = {mort}")
      print(f"Vivant = {vivant}")
      print(f"Contamine = {contamine}")
      print(f"Immunise = {immunise}")


plt.show()
    
  
#améliorations possibles :
#- mieux gérer l'aléatoire (gérer les proportions de chaque type)
#- immuniser les contaminés après un certain temps
#- optimiser la complexité du programme (trop demandant en terme de calculs)
#- liste des contaminés a chaque tour -> pouvoir les immuniser au bout de NB_TURNS_TO_LIFE

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
