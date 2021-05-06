## Jeu de l'Epidemie
Notre projet a pour but de modifier les règles du Jeu de la Vie afin de faire une simulation de la propagation d‘une épidémie au cours du temps. Dans la période actuelle, nous avons pu observer comment différents paramètres (nombre d'individus, nombre d'infectés à la base, taux de contagiosité, taux de létalité) peuvent faire varier la vitesse de propagation d’un virus et ses effets sur la population lors de la pandémie de Covid-19. C’est pourquoi, avec les modifications sur les règles générales du jeu de la vie, nous souhaitons montrer la ressemblance entre ce jeu et la vie réelle. 

Premièrement nous voulons résumer le concept du Jeu de la vie créé par John Horton Conway. Ce simple jeu de plateau a deux différentes types de cellule : noire, qui represente une cellule morte et blanc, qui represent une cellule en vie. Les règles sont simples, une cellule vivante le reste si 2 ou 3 cellules vivantes lui sont voisines, et meurt sinon, de plus, une cellule morte vit si elle a exactement 3 cellules vivantes adjacentes.

Contrairement au Jeu de la Vie, notre modèle possède plus de deux types de cellule, jous en avons introduit 4 : morte, vivante, contaminée, immunisée. L'automate cellulaire montre le changement des cellules à chaque tour et nous pouvons examiner différents résultats en changeant les critères d'évaluation. Par exemple, si il y a deux virus virus en circulation et que la probabilité de mourir après la contamination par le premier est de 0,05 mais que celle du deuxième est de 0,1. Alors, le deuxième fait diminuer la population plus rapidement. 

Cas 1: (p = 0,05)


Le nombre de mort est 650 au premier jour et est 1388 au vingtième jour. 

![fig1](https://user-images.githubusercontent.com/80094693/117318696-f4294f80-ae8a-11eb-9b11-c067e3685f46.png)
![Figure_10](https://user-images.githubusercontent.com/80094693/117318709-f7244000-ae8a-11eb-8c9c-334cb46ebe3d.png)
![Figure_20](https://user-images.githubusercontent.com/80094693/117318721-f9869a00-ae8a-11eb-848a-43b681756253.png)

(Violet = mort, bleu = vivant, vert = contaminé, jaune = immune)

Cas 2: (p = 0,1)


Le nombre de mort est 678 au premier jour et est 1684 au vingtième jour.

![Figure_11](https://user-images.githubusercontent.com/80094693/117319452-9a755500-ae8b-11eb-8379-99613656df35.png)
![Figure_100](https://user-images.githubusercontent.com/80094693/117319490-a2cd9000-ae8b-11eb-9420-af74093bb1a7.png)
![Figure_200](https://user-images.githubusercontent.com/80094693/117319499-a4975380-ae8b-11eb-8b62-ef1574d822e0.png)

(Violet = mort, bleu = vivant, vert = contaminé, jaune = immune)


Notre code crée des mondes aléatoires avec quatre types de cellules et simule la propagation du virus au cours de temps à partir d'une probabilité de mourir, d'une probabilité d'être contaminé et de la taille de notre monde. Lors du développement du modèle et des tests, nous avons donné une random seed précis, afin de corriger le code et de pouvoir faire des tests dans de bonnes conditions. Avec plus de temps et de connaissances nous aurions pu plusieurs critères et obtenir des simulations plus complexes. 




## Conway's Game of Life / Epidemic

Our project’s main focus is to manipulate the principles of Conway’s Game of Life in order to make a simulation of an epidemic over time. These days, we have the chance to observe the speed of contamination of Covid-19 and its effects on people. This is why, with our modifications, we would like to show the resemblance between this game and real life.

Brief outline of this game by John Horton Conway is that this board game has two different colors of counters, black represents death and white represents life. The rules are simple, a counter survives if it has at the most three dead neighbors and dies if there is more.  A new  counter is born if a dead counter has precisely three neighbors that are alive.

As there are more types of people affected by an epidemic in real life, we would like to increase the number of different counters from two to four : counters that are dead, alive, contaminated and immunes. The cellular automaton displays the change of counters in every round and we can obtain different results by changing the conditions. For example, if there are two types of deadly viruses and the probability of the first one is 0,05 but the second one is even deadlier and the probability is 0,1. In this case, the second virus will decrease the population faster.

Hence, our code creates random worlds with four different types of cells and simulates the propagation of a virus over time according to the threshold of death, to the threshold of contamination and to the size of the world. The results are different because the world is created randomly so the position of the first contaminated cell, the number of death cells and immune cells change randomly every time. With subtle improvements of the code, we can add more conditions and achieve complex simulations.



## Présentation de l'equipe :

Dilyara BABANAZAROVA

Simay CELIK

Alexis DUCOTTET

Yanni LEFKI

## Description synthétique du projet

**Problématique :**
La contagiosité d’un virus affecte-t-elle la vitesse de la propagation du virus?

**Hypothèse :**
La vitesse de la propagation d'un virus est liée à sa contagiosité.

**Objectif(s) :**
Faire varier les conditions afin d'observer la propagation d'une epidémie au cours du temps à l'aide de jeu de la vie.

**Critère(s) d'évaluation :**

-Les coordonnés du premier infecté

-Le nombre de contamination par personne

 -Seuil de contamination

 -Seuil de mort après contamination

-Densité de population

-Regroupement des immunes 


## Lien vers notre code :

<a href= "https://github.com/ARE-2021-GR3/jeu_de_la_vie/blob/main/code.py" > C'est ici notre code ! </a>


## Lien vers page de blog :
Nous avons crée un blog afin de documenter l'avancement du projet.

<a href= "https://github.com/ARE-2021-GR3/jeu_de_la_vie/blob/main/blog.md">   C'est ici notre blog ! </a>



## Bibliographie :

Caballero, Lorena, Robert Hodge, and Sergio Hernandez. “Conway’s ‘Game of Life’ and the Epigenetic Principle.” Frontiers in Cellular and Infection Microbiology 6 (June 14, 2016). https://doi.org/10.3389/fcimb.2016.00057.

“Conway’s Game of Life.” In Wikipedia, March 25, 2021. https://en.wikipedia.org/w/index.php?title=Conway%27s_Game_of_Life&oldid=1014218578.

“La Propagation d’une Épidémie.” Accessed March 27, 2021. http://www.tangentex.com/ACEpidemie.htm.
Li, Ruiqi, Peter Richmond, and Bertrand Roehner. “Effect of Population Density on Epidemics,” 2018.

“Mathematical Games - The Fantastic Combinations of John Conway’s New Solitaire Game ‘Life’ - M. Gardner - 1970,” 1970, 6.

Oxman, Gadi, Shlomo Weiss, and Yair Be’ery. “Computational Methods for Conway’s Game of Life Cellular Automaton.” Journal of Computational Science 5, no. 1 (2014): 24–31. https://doi.org/10.1016/j.jocs.2013.07.005.

SUN, GUI-QUAN, ZHEN JIN, and LI LI. “EMERGENT TURING PATTERN IN EPIDEMIC SPREADING USING CELLULAR AUTOMATON.” International Journal of Modern Physics B, April 7, 2012. https://doi.org/10.1142/S0217979211059401.

Zhang, Deguo. “Un automate cellulaire de l’espace réel pour l’étude des populations de dunes.” Thèse de doctorat, Institut de physique du globe, 2011.




