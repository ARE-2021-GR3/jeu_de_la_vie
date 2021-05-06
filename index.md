## Jeu de l'Epidemie
Notre projet a pour but de manipuler les principes de Jeu de la vie afin de faire une simulation de la propagation d‘une épidémie au cours du temps. Désormais, nous avons pu observer comment les conditions peuvent faire varier la vitesse de propagation d’un virus et ses effets sur la population lors de la pandémie de Covid-19. C’est pourquoi, avec les modifications sur les règles générales du jeu de la vie, nous pouvons montrer la ressemblance entre ce jeu et la vie réelle. 

Premièrement nous voulons résumer le concept du Jeu de la vie créé par John Horton Conway. Ce simple jeu de plateau a deux différentes types de cellule : noir qui represent la morte et blanc qui represent la vie. Les règles sont simples, la cellule survit si elle a au plus trois cellules voisines mortes et meurt sinon. Une nouvelle cellule est née si une cellule morte a précisément trois voisins vivants.

Nous voulons augmenter les types de cellules parce que normalement il y a plusieurs possibilités au cours d’une pandémie.Il n’y a pas seulement deux types mais il y a des cellules mortes, vivantes, contaminées, immunes etc.. Notre automate cellulaire montre le changement des cellules à chaque tour et nous pouvons examiner différents résultats en changeant les critères d'évaluation. Par exemple, il y a deux virus et la probabilité de mourir après la contamination du premier est 0,05 mais le deuxième est plus fatal et la probabilité de mourir est 0,01. Dans ce cas-là, la population diminue plus rapidement. 

Ainsi, notre code crée des mondes aléatoires avec quatre types de cellules et simule la propagation du virus au cours de temps à partir de seuil de mortalité, de seuil de contamination, de taille du monde. Les resultats different chaque fois car le monde est aléatoire et la position du premier contaminée, le nombre de cellules mortes et de cellules immunisées changent aléatoirement aussi. Avec le développement du code, on pourrait ajouter plusieurs critères et obtenir des simulations plus complexes. 

*** images d'Exemple a mettre


## Conway's Game of Life / Epidemic
(english version) 

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
Faire varier les conditions afin d'observer la propagation d'une epidémie au cours du temps à l'aide de jau de la vie.

**Critère(s) d'évaluation :**

-Les coordonnés du premier infecté

-Le nombre de contamination par personne

 -Seuil de contamination

 -Seuil de mort après contamination

-Densité de population

-Regroupement des immunes 


## Lien vers le page du code :

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




