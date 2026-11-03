# Projet d'Outils Fondamentaux - BUT1 Informatique

**Auteure :** Rokhaya FALL  
**Formation :** BUT1 Informatique 
**Établissement :** IUT Nord Franche-Comté  

---

## 1. Introduction et Objectifs du Projet

Ce dépôt regroupe les travaux pratiques organisés dans le dossier **tp/** ainsi qu'un projet personnel réalisés dans le cadre du module (dossier **projet/**).

Le projet consiste à développer un **simulateur et analyseur de prêts immobiliers**. 
L'objectif est de mettre en pratique les notions théoriques et algorithmiques abordées en TP à travers un cas d'application concret, en combinant :
* La résolution de systèmes linéaires par le calcul matriciel.
* La recherche de racines numériques pour des polynômes financiers.
* L'intégration numérique pour l'évaluation de coûts.

## 2. Intégration des Notions de TP dans le Projet

Le code du projet s'articule autour de trois grands blocs directement issus des compétences développées en TP :

**a) Algèbre linéaire et matrices:** Le projet intègre une fonction de résolution de systèmes linéaires basée sur l'algorithme du pivot de Gauss avec recherche de pivot partiel. Cette approche est utilisée pour modéliser et résoudre un problème d'allocation budgétaire ou de répartition financière préalable. 

**b) Recherche de racines et polynômes:** Le cœur du simulateur repose sur la résolution d'un polynôme financier reliant le capital emprunté, la durée et les mensualités afin de déterminer le taux d'intérêt exact. 
Deux méthodes ont été implémentées et comparées : la méthode de la Dichotomie et la méthode de Newton.

**c) Intégration numérique:** L'estimation du coût cumulé des intérêts payés à la banque au fil du temps est réalisée à l'aide de la méthode des trapèzes, permettant d'approcher l'aire sous la courbe d'amortissement de manière discrète.

## 4. Résultats de l'Exécution

Prêt immobilier :

Capital emprunté : $180\,000$ € -- 
Mensualité : $1\,000$ € --
Durée : $240$ mois (20 ans)

Résultats affichés dans la console:

=== PARTIE MATRICIELLE (SYSTEME LINEAIRE) ===

Répartition des investissements : [12500.0, 15000.0, 8125.0]

=== PARTIE FINANCIERE (TAUX DE PRET) ===

**Dichotomie :** Taux annuel = 3.826% (28 itérations) -- 
**Newton     :** Taux annuel = 3.826% (4 itérations) --  
**Coût total estimé des intérêts (Trapèzes) :** 73150.42 €

En complément, le script génère une visualisation graphique via matplotlib illustrant l'évolution du nombre d'itérations des deux méthodes de recherche de racines selon différentes hypothèses de mensualités.

## 5. Analyse Critique et Observations

L'expérimentation montre l'efficacité de la méthode de Newton, qui converge en seulement 4 itérations face aux 28 étapes nécessaires pour la dichotomie. Cependant, il a été observé que Newton requiert de bonnes conditions initiales pour éviter des problèmes de divergence (notamment si la dérivée s'annule), ce qui met en valeur la complémentarité des deux méthodes.

## 6. Utilisation de l'Intelligence Artificielle

J'ai utilisé une intelligence artificielle pour générer la structure et le code principal de ce projet. J'ai entièrement dirigé ce processus en l'orientant et en y apportant des modifications ciblées pour m'assurer que le tout correspondait précisément à mes attentes et aux méthodes vues en TP.


