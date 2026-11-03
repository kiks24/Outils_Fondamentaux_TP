#Exercice 1.1: La liste des diviseurs

def diviseurs(n):
    liste = []
    for d in range(1,n + 1):
        if (n % d == 0):
            liste.append(d)
    return liste
    

print(diviseurs(28))


#Exercice 2.1: Les deux PGCD

def pgcd_naif(a,b):
    pgcd = 1
    for i in range(1, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            pgcd = i
    return pgcd

print(pgcd_naif(1071, 462))

def pgcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a 

print(pgcd(1071,462))

        
#Exercice 3.1

def est_premier_naif(n):
    """Teste la primalité en essayant tous les diviseurs jusqu'à n - 1."""
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

print(est_premier_naif(97), est_premier_naif(91))

def est_premier(n):
    """Teste la primalité en s'arrêtant à la racine carrée de n."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True

print(est_premier(97), est_premier(91), est_premier(2), est_premier(1))

import time

def duree(fonction, argument):
    """Renvoie le temps d'exécution de fonction(argument), en secondes."""
    debut = time.perf_counter()
    fonction(argument)
    return time.perf_counter() - debut

for n in [10_007, 100_003, 1_000_003]:
    print(f"naif        : {duree(est_premier_naif, n):.4f} s")
    print(f"jusqu'a rac : {duree(est_premier, n):.6f} s")

#Exercice 4.1

def crible(limite):
    """Renvoie la liste des nombres premiers de 2 à limite inclus."""
    est_premier_tab = [True] * (limite + 1)
    est_premier_tab[0] = False
    if limite >= 1:
        est_premier_tab[1] = False
    d = 2
    while d * d <= limite:
        if est_premier_tab[d]:
            for multiple in range(d * d, limite + 1, d):
                est_premier_tab[multiple] = False
        d = d + 1
    return [n for n in range(limite + 1) if est_premier_tab[n]]


print(f"crible       : {len(crible(100_000))} nombres premiers pour {duree(crible, 100_000):.4f} s")

Duree = 0
n_premiers = 0
for n in range(1, 100_000):   
    Duree += duree(est_premier, n)
    if est_premier(n):
        n_premiers += 1

print(f"est_premier      : {n_premiers} nombres premiers pour {Duree: .4f} s")
    
#Exercice 5.1

def facteurs(n):
    liste = []
    for i in range(2, n + 1):
        if est_premier(i):
            while n % i == 0:
                liste.append(i)
                n = n // i 
    return liste

print(facteurs(360))

produit = 1
for i in (facteurs(360)):
    produit *= i
print (produit)

#Exercice 6.1

def fibonacci_recursif(n):
    """F(n) en suivant la définition, par récurrence."""
    if n < 2:
        return n
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

print([fibonacci_recursif(n) for n in range(15)])

for n in (20, 25, 30):
    print(f"fibonnaci_recursif({n})     : {duree(fibonacci_recursif, n): .4f} s")

#Exercice 6.2

compteur = {}
def fibonacci_appels(n):
    compteur[n] = compteur.get(n, 0) + 1
    """F(n) en suivant la définition, par récurrence."""
    if n < 2:
        return n
    return fibonacci_appels(n - 1) + fibonacci_appels(n - 2)

print(fibonacci_appels(30))
print(compteur[1])


#Exercice 6.3

def fibonnaci(n):
    precedente , courante = 0, 1
    for i in range(n):
        precedente , courante = courante, precedente + courante
    return precedente

print(all(fibonnaci(n) == fibonacci_recursif(n) for n in range(1,25)))
print(f"{len(str(fibonnaci(10_000)))} chiffres pour {duree(fibonnaci, 10_000): .6f} s")

#Exercice 7.1

def euclide_etendu(a, b):
    if b == 0:
        return a, 1, 0
    g, u, v = euclide_etendu(b, a % b)
    return g, v, u - (a // b) * v  

print(euclide_etendu(1071, 462))
g, u, v = euclide_etendu(1071, 462)
print(f"1071 * {u} + 462 * {v} = {1071 * u + 462 * v} ")

#Exercice 7.2

def puissance_mod_naive(a, e, n):
    resultat = 1
    for _ in range(e):
        resultat = resultat * a % n
    return resultat

def puissance_mod(a, e, n):
    resultat = 1
    a = a % n
    while e > 0:
        if e % 2 == 1:
            resultat = resultat * a % n
        a = a * a % n
        e = e // 2
    return resultat

a, e, n = 7, 10  ** 7, 1_000_003
print(puissance_mod_naive(a, e, n))
print(puissance_mod(a, e, n))
print(pow(a, e, n))

debut = time.perf_counter()
puissance_mod_naive(a, e, n)
t_naive = time.perf_counter() - debut
debut = time.perf_counter()
puissance_mod(a, e, n)
t_rapide = time.perf_counter() - debut
print(f"naive {t_naive:.3f} s | rapide {t_rapide:.6f} s")
