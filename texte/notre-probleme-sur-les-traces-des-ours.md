Imaginons que vous souhaitez étudier la population d'ours dans une région.[^exemple] En particulier, vous cherchez à déterminer la répartition des âges, par exemple pour vous assurer que la population se renouvelle bien.

[^exemple]: Cet exemple est fictif, tout comme les données présentées plus bas.

Seulement c'est l'hivers, il fait froid et vous rechignez à l'idée de passer de longues heures dehors en quête d'ours probablement blottis au fond d'une caverne. Vous décidez donc de ruser et de vous rendre au lac où ils s'abbreuvent. Là-bas, vous pourrez observer les empreintes et peut-être en déduire l'âge des individus.

En effet, il semble probable que la taille des empreintes et l'âge des animaux soient corrélés, c'est-à-dire dépendants l'un de l'autre.[^causalite] Le cas échéant, mesurer la première vous fournirait des informations sur le second. Pour vous en assurer, vous pouvez vous baser sur les données que vous récoltez depuis plusieurs années sur les ours, stockées dans un fichier au [format CSV](https://fr.wikipedia.org/wiki/Comma-separated_values) :

[^causalite]: Attention à ne pas confondre corrélation et causalité, comme expliqué dans [cette vidéo](https://www.youtube.com/watch?v=lg2hFq9RlYM).

TODO : lien vers le fichier csv

```
# Taille d'empreinte (cm), âge (années)
TODO
...
```

Une très bonne habitude quand on étudie des données est de les représenter graphiquement :

```python

```

![TODO]()

[[question]]
| Pourquoi représenter l'âge en fonction de la taille des empreintes et non l'inverse ?

N'oubliez pas votre objectif : estimer l'âge d'un individu à partir de la taille de son empreinte. TODO: terminologie https://fr.wikipedia.org/wiki/R%C3%A9gression_lin%C3%A9aire#Terminologie Parler de feature

Manifestement, vos deux variables sont bien corrélées. Dans le cas contraire, nous aurions obtenu un graphe où les points auraient semblé aléatoires, sans motif particulier. Ici, les données se répartissent clairement autour d'une droite.

Que faire maintenant ? Rappelez-vous que vous voulez faire de la prédiction. Par exemple, imaginons qu'en vous promenant vous tombiez sur une empreinte de TODO cm. Avec l'aide du graphe représenté plus haut, il est assez simple d'estimer l'âge de l'individu :

![Image TODO]()

En l'occurrence, il apparaît plausible que l'ours ait TODO ans. Mais est-il vieux de TODO années ou de TODO ? Peut-on déterminer rigoureusement quelle est la meilleure estimation possible ?

Pour répondre à ces questions, nous devons formaliser le raisonnement suivi et introduire la notion de modèle.