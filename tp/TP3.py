#Exercice 1.1 : Evaluation naÏve 

def evaluer_naif(P,x):
    polynome = 0
    for i in range (0, len(P)):
        polynome +=  P[i] * (x ** i)
    return polynome

#print(evaluer_naif([2,3,0,5], 2))

#Exercice 2.1 : Horner

def evaluer(P,x):
    polynomeH = 0
    for i in range(-1, -len(P)-1, -1):
        polynomeH = polynomeH * x + P[i]
    return polynomeH

#print(evaluer([2,3,0,5], 2))

#Exercice 2.2 : meesurer et se méfier de ses prévisions

import time 

P1 = []
for i in range(1000):
    P1.append(1)

P2 = []
for i in range(5000):
    P2.append(1)

P3 = []
for i in range(20000):
    P3.append(1)

for P in (P1, P2, P3):
    debut = time.perf_counter()
    evaluer_naif(P, 1.0001)
    naif = time.perf_counter() - debut

    debut = time.perf_counter()
    evaluer(P, 1.0001)
    horner = time.perf_counter() - debut

    #print(f"naif : {naif:.6f} s - horner : {horner:.6f} s / rapport : {naif / horner:.1f}")

    #Exercice 2.3

    import time 

P1 = []
for i in range(200):
    P1.append(1)

P2 = []
for i in range(400):
    P2.append(1)

P3 = []
for i in range(800):
    P3.append(1)

for P in (P1, P2, P3):
    debut = time.perf_counter()
    evaluer_naif(P, 3)
    naif = time.perf_counter() - debut

    debut = time.perf_counter()
    evaluer(P, 3)
    horner = time.perf_counter() - debut

    #print(f"naif : {naif:.6f} s - horner : {horner:.6f} s / rapport : {naif / horner:.1f}")

#Exercice 3.1

def deriver(P):
    P_prime = []
    for i in range (1, len(P)):
        P_prime.append(i * P[i])
    return P_prime

#print(deriver([2, 3, 0, 5]))

#Exercice 4.1

import math

def dichotomie(f, a, b, tolerance):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b 
    if f(a) * f(b) > 0:
        raise ValueError(f"f(a) et f(b)doivent être de signes opposés.")
    while(b - a) / 2 > tolerance:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b ) / 2

def f(x):
    return x ** 2 - 2

racine = dichotomie(f, 0, 2, 1e-6)
#print(racine)


#Exercice 4.2

def newton(P, depart, tolerance):
    x = depart
    tours = 0
    while abs(evaluer(P,x)) > tolerance:
        val_P = evaluer(P,x)
        val_P_prime = evaluer(deriver(P), x)
        if val_P_prime == 0:
            raise ValueError("Dérivée nulle")
        x = x - val_P / val_P_prime
        tours += 1
    return x, tours

P = [-5, -2, 0, 1]
racine, tours = newton(P, 2, 1e-6)
#print(f"racine : {racine} en {tours} tours.")


#Exercice 4.3

def newton_trajet(P, depart, tolerance):
    x = depart
    tours = 0
    while abs(evaluer(P,x)) > tolerance:
        val_P = evaluer(P,x)
        val_P_prime = evaluer(deriver(P), x)
        if val_P_prime == 0:
            raise ValueError("Dérivée nulle")
        x = x - val_P / val_P_prime
        tours += 1
    return x, tours


Q = [2, -2, 0, 1]
#print(newton(Q, 0, 1e-6))


#Exercice 4.4

def newton(P, depart, tolerance):
    x = depart
    tours = 0
    while abs(evaluer(P,x)) > tolerance:
        val_P = evaluer(P,x)
        val_P_prime = evaluer(deriver(P), x)
        if val_P_prime == 0:
            raise ValueError("Dérivée nulle")
        x = x - val_P / val_P_prime
        tours += 1
    return x, tours

P = [-5, -2, 0, 1]
racine, tours = newton(P, 2, 1e-6)
racine2, tours2 = newton(P, 0, 1e-6)
#print(f"racine : {racine} en {tours} tours depuis 2 contre {tours2} tours depuis 0")


#Exercice 5.1

#import matplotlib.pyplot as plt

Q = [-5, -2, 0, 1]          # x^3 - 2x - 5
xs = [i / 100 for i in range(-300, 301)]
ys = [evaluer(Q, x) for x in xs]

#plt.figure()
#plt.plot(xs, ys, label="x^3 - 2x - 5")
#plt.axhline(0, linewidth=0.8)
#plt.axvline(0, linewidth=0.8)
#plt.ylim(-20, 20)
#plt.xlabel("x")
#plt.ylabel("P(x)")
#plt.legend()
#plt.title("Un polynome et son unique racine reelle")
#plt.show()


#Exercice 6.1

def somme(P,Q):
    liste_somme = []
    longueur = max(len(P), len(Q))
    while len (P) < longueur:
        P.append(0)
    while len(Q) < longueur:
        Q.append(0)

    for i in range (longueur):
        liste_somme.append(P[i] + Q[i])
    return liste_somme 

def produit_poly(P, Q):
    liste_produit = []
    if P == [] or Q == []:
        return []
    longueur = len(P) + len(Q) - 1
    for _ in range(longueur):
        liste_produit.append(0)
    for j in range(len(P)):
        for k in range(len(Q)):
            termes = P[j] * Q[k]
            liste_produit[j + k] = liste_produit[j + k] + termes

    return liste_produit

#print(somme([1, 2], [0, 0, 3]))
#print(produit_poly([1, 1], [1, 1]))
#print(produit_poly([-1, 1], [1, 1]))

#Exercice 6.2

P = [1, 1]
for i in range(9):
    P = produit_poly(P, [1, 1])
#print(P)

#Exercice 7.1

import math

def derivee_avant(f, x, h):
    return (f(x + h) - f(x)) / h

def derivee_centree(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

f = math.sin
derivee_exacte = math.cos
x = 1.0

valeurs_h = [1e-1, 1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12]
for h in (valeurs_h):
    approx_avant = derivee_avant(f, x, h)
    approx_centree = derivee_centree(f, x, h)
    exacte = derivee_exacte(x)
    erreur_avant = abs(approx_avant - exacte)
    erreur_centree = abs(approx_centree - exacte)
    #print(f"h = {h:.0e} : avant {erreur_avant:.1e} | centree {erreur_centree:.1e}")


#Exercice 8.1

def rectangle(f, a, b, n):
    h = (b - a ) / n
    somme_val = 0
    for i in range(n):
        x = a + i * h 
        somme_val += f(x)
    return h * somme_val

def trapezes(f, a, b, n):
    h = (b - a) / n 
    interieur = 0
    for i in range(1, n):
        x = a + i * h 
        interieur  += f(x)
    return h * ((f(a) + f(b)) / 2 + interieur)

def simpson(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    impairs = 0
    for i in range(1, n, 2):
         x = a + i * h 
         impairs += f(x)
    pairs = 0
    for i in range(2, n, 2):
         x = a + i * h 
         pairs += f(x)

    return h / 3 * (f(a) + f(b) + 4 * impairs + 2 * pairs)

def carre(x):
    return x ** 2

valeur_exacte = 1 / 3

for n in (10, 100, 1000):
    res_rect = rectangle(carre, 0, 1, n)
    erreur_rect = abs(res_rect - valeur_exacte)

    res_trap = trapezes(carre, 0, 1, n)
    erreur_trap = abs(res_trap - valeur_exacte)

    res_simp = simpson(carre, 0, 1, n)
    erreur_simp = abs(res_simp - valeur_exacte)

    #print(f"n = {n:>4} : rectangles {erreur_rect:.1e} | trapezes {erreur_trap:.1e} | simpson {erreur_simp:.1e}")    

#Exercice 8.2
    
def arctangente_derivee(x):
    return 4 / (1 + x * x)


n = 1000
trap = trapezes(arctangente_derivee, 0, 1, n)
simp = simpson(arctangente_derivee, 0, 1, n)

print(f"Trapèzes : {trap} | Erreur : {abs(trap - math.pi)}")
print(f"Simpson  : {simp} | Erreur : {abs(simp - math.pi)}")
