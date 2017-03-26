Pour faire mieux au cours du temps, encore faut-il pouvoir s'évaluer.

# La fonction d'erreur

En machine learning, on ne cherche pas à mesurer à quel point un modèle est bon, mais combien il est mauvais. L'objectif est alors de minimiser la valeur mesurée, pour obtenir un modèle le moins mauvais possible.

L'outil mathématique faisant office de mesure est une fonction $e$, appelée fonction d'erreur (ou de perte), dont les paramètres sont ceux du modèle. Dans notre cas, ce sont les réels $a$ et $b$ :

$$
TODO
$$

La fonction d'erreur compare la valeur du jeu d'entrainement avec celle du modèle. 

Au fil des années, une grande variété de fonctions d'erreur ont vu le jour. Je vais toutefois me contenter ici de vous présenter celle utilisée classiquement pour la régression linéaire : la méthode des moindres carrés. Notre fonction d'erreur a alors l'expression suivante :

$$
TODO
$$

Explication en français + visualisation avec des carrés

Bien, maintenant que nous sommes capables de mesurer l'erreur, il nous faut déterminer quels paramètres $a$ et $b$ permettent de la minimiser. Nous étudions cela dans la prochaine section.

* Tracer la fonction d'erreur et permettre au lecteur de jouer avec les paramètres pour voir comment ça influe sur l'erreur
* Notion de précision
* jeu d’entrainement/jeu de test : ce serait comme avoir en examen un exercice déjà fait en classe : ce n’est pas parce qu’on a une bonne note qu’on a assimilé les notions sous-jacentes