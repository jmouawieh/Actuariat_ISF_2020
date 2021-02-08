# Actuariat_ISF_2020


Enoncé: 

Tarification en assurance IARD avec des modèles de régression
L’assurance est un contrat par lequel, moyennant le versement d’une prime dont le montant est fixé
a priori (en début de période de couverture), l’assureur s’engage à indemniser l’assuré pendant toute
la période de couverture (disons un an). Cette prime est censée refléter le risque associé au contrat.
Pour chaque police d’assurance, la prime est une fonction de variables dites tarifaires (permettant de
segmenter la population en fonction de son risque). Le but de ce projet est de proposer un tarif en se
basant sur l’approche fréquence – sévérité et les modèles de régression. Au moins deux modèles
doivent être testés.

Les documents :

1 - Base de 100 000 polices *-PG 2017 YEAR0.csv et d’une base de sinistres associés *-PG 2017 CLAIMS YEAR0.csv 
qui permettent de calibrer le modèle. (Matthieu&Jade-PG_2017_YEAR0.csv) <br>
2 - La base de validation de 100 000 polices *-PG 2017 CLAIMS YEAR1.csv. (Matthieu&Jade-PG_2017_YEAR1.csv) <br>
3 - Les données sont issues d’un jeu de tarification actuarielle : elles sont décrites en détails dans le document 
description_variables.pdf<br>
4 - Le rapport (Projet_tarification_Jade_Matthieu (3).pdf) synthétique et organisé présentant la méthodologie utilisée et les résultats<br>
5 - un fichier R principal appelant le code utilisé dans le rapport et commenté brièvement. (projet J&M.Rmd)<br>
6 - un fichier csv TARIF.csv avec les tarifs proposés. (base_tarif.csv)<br>

On a:
1. Explorez les données *YEAR0.csv.
2. Présenter la méthodologie utilisée (lois calibrées, variables retenues, adéquation,etc ).
3. Présenter les résultats et conclure sur le modèle le plus approprié.
4. Donnez notre tarif pour les polices des données de validation.

Projet encadré par Madame Julia SIMAKU et effectué en collaboration avec Matthieu Hobeika.

Jade Mouawieh.
