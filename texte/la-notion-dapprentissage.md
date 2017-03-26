De manière classique, pour résoudre un problème informatique on fournit à la machine une **suite précise d'instructions** à exécuter, appelée algorithme. Par exemple, le plus ancien connu aujourd'hui est l'[algorithme d'Euclide](https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide) :

```python
def euclide(a, b):
    # a et b sont deux entiers naturels non nuls
    # a >= b
    r = a%b # r est le reste de la division entière de a par b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b
```

Autrement dit, nous indiquons à la machine comment produire le résultat attendu à partir d'un certain nombre de paramètres. En quelque sorte, nous fournissons une recette de cuisine. Seulement, cette démarche se heurte à la **complexité** et à la **diversité** de certains problèmes.

Par exemple, TODO truc complexe.

Pour ce qui est de la diversité, imaginez que vous devez apprendre à un enfant ce qu'est un arbre. Vous pourriez mentionner la forme rectiligne d'un tronc, la texture rugueuse d'une écorce, la couleur verte des feuilles, etc... Toutefois, vous vous rendriez vite compte qu'il y a **trop de paramètres** : toutes les espèces n'ont pas la même texture ou couleur d'écorce, les connifères n'ont pas de feuilles, tout comme les feuillus en hivers... Ainsi, si vous deviez apprendre à un enfant ce qu'est un arbre, il est probable que vous le feriez plutôt à l'aide d'**exemples**.

![Il existe une grande diversité derrière le mot « arbre ».]()

Le *machine learning*, c'est en partie ça. En partie seulement parce que, comme nous le verrons en fin de tutoriel, nous ne sommes pas toujours en mesure de fournir des exemples. Plus généralement donc, le *machine learning* c'est faire en sorte que la machine apprenne à effectuer un travail **par l'expérience**. 

TODO: notion d'évaluation puis d'amélioration

Pour assimiler ces notions, le plus efficace est de jouer avec ; intéressons-nous donc à un cas d'application.
___________________

* On a un jeu de données

Surtout une question de vocabulaire. En soi, c'est juste de l'optimisation

Parfois, nous ne sommes même pas capable de décrire le phénomène étudié. Pensez à la médecine.

Donner des exemples = entrainement supervisé. Je présente d'autres méthodes d'apprentissage en fin de tutoriel.