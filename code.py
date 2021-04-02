import matplotlib.pyplot as plt
import numpy as np
import random

matrice = np.array([[0, 1, 1, 1, 0],
                    [1, 0, 1, 0, 0], 
                    [0, 0, 1, 1, 0],
                    [0, 1, 1, 0, 1],
                    [1, 0, 1, 1, 0]])


def voisinnage(matrice, el): #matrice : List[List[int]], el : Tuple[int, int], neigh : int
    """Renvoie une liste d'indices des éléments dans
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
    
    return res


    #cas 6 (bord haut)
    elif (yEl == 0):
        #à gauche
        res.append(0, yEl-1)
        #à droite
        res.append(0, yEl+1)
        #en bas
        
        
    #cas 7 (bord gauche)
    elif (yEl == 0):
        #en haut
        res.append((xEl-1, 0))
        res.append((xEl-1, 1))
