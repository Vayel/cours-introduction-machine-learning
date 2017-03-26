Cette dernière décennie, la quantité de données informatiques à disposition a tout bonnement explosé. Aujourd'hui, tout le monde est en permanence connecté via son *smartphone* et transmet volontairement ou non des informations par le biais de multiples applications, auxquelles s'ajoutent les objets connectés apparaissant un peu partout. Qui plus est, les données deviennent de plus en plus accessibles, avec des bases de données ouvertes telles que [ImageNet](http://www.image-net.org/).

En parallèle à ces phénomènes, les capacités de stockage et de calcul de nos machines ont largement augmenté, notamment grâce à l'industrie du jeu vidéo, induisant un développement fulgurant de l'intelligence artificielle et plus particulièrement du *machine learning*, un de ses sous-domaines. Ce dernier s'illustre au travers de multiples applications tout à fait remarquables : [AlphaGo](https://fr.wikipedia.org/wiki/AlphaGo), l'IA de la société DeepMind[^deepmind] ayant battu un des meilleurs joueurs de Go au monde, les voitures autonomes, la [reconnaissance d'images](https://cloud.google.com/vision/), l'interprétation de texte, etc. Le *machine learning* est même présent dans l'art :

![Image générée par [DeepArt](https://deepart.io/) à partir d'une capture d'écran du film *The Hobbit* de Peter Jackson.](/media/galleries/2924/1416b6df-6372-4fd1-a1fb-8f97d5dcdbc2.jpg)

[^deepmind]: Rachetée par Google en 2014.

Comme le nom l'indique, le *machine learning* (ML) consiste à faire apprendre à une machine un travail plutôt que de lui fournir des instructions pour l'effectuer. Ça fait rêver, n'est-ce pas ? Mais, même si les possibilités semblent immenses, comprenez bien que le *machine learning* n'est pas magique et ne permet pas de résoudre tous les problèmes : il s'agit d'un regroupement de concepts mathématiques et d'algorithmes qui peuvent être appliqués, ou non, selon le contexte du problème posé.

Ce tutoriel se veut introductif. Son objectif n'est pas de vous enseigner en profondeur les algorithmes et concepts mathématiques mentionnés, mais de vous fournir une vue d'ensemble sur le domaine au travers d'un exemple et de vous faire assimiler les notions de base par la pratique. Pour ce faire, nous analyserons un problème et tenterons de le résoudre à l'aide d'un outil mathématique appelé régression linéaire, que nous implémenterons avec le langage Python[^python]. Une maîtrise de ce dernier est un plus mais n'est pas obligatoire, les programmes présentés pouvant facilement se réécrire dans un autre langage. Il est même possible de suivre ce tutoriel sans prêter attention au code et se concentrer uniquement sur le raisonnement et les outils mathématiques.

[^python]: Ce langage est très présent dans le monde du *machine learning*, notamment au travers des bibliothèques [scikit-learn](http://scikit-learn.org/stable/index.html) et [Tensorflow](https://www.tensorflow.org/).

[[i]]
| **Prérequis**  
| Fonctions mathématiques.
|
| **Prérequis optionnels**  
| Bases en programmation (variables, structures de contrôle, fonctions, listes).  
| Expérience avec le langage Python.
|
| **Objectif**  
| Assimiler les concepts de base du *machine learning* par l'étude pratique d'un problème de régression.  
|
| **Aspects non traités**  
| Détail des algorithmes d'apprentissage.  
| Pré-traitement des données.  
| Choix de l'algorithme d'apprentissage.