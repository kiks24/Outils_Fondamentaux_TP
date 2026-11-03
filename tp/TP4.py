#Exercice 1.1 

def transposee(A):
    lignes, colonnes = len(A), len(A[0])
    echange = []
    for j in range (colonnes):
        nouvelle_ligne = []
        for i in range (lignes):
            nouvelle_ligne.append(A[i][j])
        echange.append(nouvelle_ligne)
    return echange

#print(transposee([[1, 2, 3], [4, 5, 6]]))

#Exercice 2.1

def produit(A, B):
    n = len(A)
    p = len(A[0])
    q = len(B[0])
    C = [[0] * q for _ in range(n)]
    for i in range(n):
        for j in range(q):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]     
    return C

identite = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
A = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]
#print(produit(A, identite) == A)
#print(produit([[1, 2], [3, 4]], [[0, 1], [1, 0]]))

#Exercice 2.2

import random
import time

random.seed(42)

def matrice_aleatoire(n):
    matrice = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(random.random())
        matrice.append(ligne)
    return matrice

for n in (40, 80, 120):
    A = matrice_aleatoire(n)
    B = matrice_aleatoire(n)
    debut = time.perf_counter()
    produit(A, B)
    fin = time.perf_counter()

    print(f"n = {n:>3} : {fin - debut:.4f} s")

#Exercice 3.1

import numpy as np

A = matrice_aleatoire(n)
B = matrice_aleatoire(n)

debut = time.perf_counter()
produit(A, B)
python = time.perf_counter() - debut

Anp = np.array(A)
Bnp = np.array(B)

debut = time.perf_counter()
Anp @ Bnp
numpy = time.perf_counter() - debut


print(f"python pur {python:.4f} s")
print(f"numpy      {numpy:.6f} s")
print("rapport :", round(python / max(numpy, 1e-9)))

#Exercice 4.1

def resoudre(A, b, tolerance=1e-14):
    n = len(A)
    
    M = []
    for i in range(n):
        ligne = []
        for j in range(len(A[i])):
            ligne.append(A[i][j])
        ligne.append(b[i])
        M.append(ligne)
        
    for k in range(n):
        meilleure = k
        valeur_max = abs(M[k][k])
        for i in range(k + 1, n):
            if abs(M[i][k]) > valeur_max:
                valeur_max = abs(M[i][k])
                meilleure = i
                
        if abs(M[meilleure][k]) <= tolerance:
            raise ValueError("systeme singulier ou mal pose")
            
        temp = M[k]
        M[k] = M[meilleure]
        M[meilleure] = temp
        
        for i in range(k + 1, n):
            facteur = M[i][k] / M[k][k]
            for j in range(k, n + 1):
                M[i][j] = M[i][j] - facteur * M[k][j]
                
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        somme = M[i][n]
        for j in range(i + 1, n):
            somme = somme - M[i][j] * x[j]
        x[i] = somme / M[i][i]
        
    return x


A = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]
b = [2, -1, 8]
x = resoudre(A, b)

x_arrondi = []
for v in x:
    x_arrondi.append(round(v, 10))
print(x_arrondi)

verif = []
for i in range(3):
    somme_ligne = 0
    for j in range(3):
        somme_ligne = somme_ligne + A[i][j] * x[j]
    verif.append(round(somme_ligne, 10))
print(verif)

#Exercice 4.2

random.seed(7)
n = 50
A = matrice_aleatoire(n)
b = [random.random() for _ in range(n)]

solutuion = resoudre(A, b)
numpy_solution = np.linalg.solve(np.array(A), np.array(b))

ecart = max(abs(solutuion[i] -numpy_solution[i]) for i in range(n))
print("ecart maximal :", ecart)
print(ecart < 1e-9)

#Exercice 5.1

def hilbert(n):
    return np.array([[1.0 / (i + j + 1) for j in range(n)] for i in range(n)])

n = 12
H = hilbert(n)
x_vrai = np.ones(n)          # on choisit la solution d'avance
b = H @ x_vrai               # et on fabrique le second membre correspondant

x_solve = np.linalg.solve(H, b)
x_inverse = np.linalg.inv(H) @ b

print("erreur avec solve   :", float(np.max(np.abs(x_solve - x_vrai))))
print("erreur avec inv @ b :", float(np.max(np.abs(x_inverse - x_vrai))))
print("conditionnement     : {:.3e}".format(float(np.linalg.cond(H))))

#Exercice 6.1

import matplotlib.pyplot as plt

def rotation(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s], [s, c]])

# une maison, comme suite de points (fermée)
maison = np.array([[0, 0], [2, 0], [2, 1.5], [1, 2.5], [0, 1.5], [0, 0]]).T

plt.figure(figsize=(5, 5))
plt.plot(maison[0], maison[1], label="depart")
for angle in (np.pi / 6, np.pi / 3, np.pi / 2):
    image = rotation(angle) @ maison
    plt.plot(image[0], image[1], label=f"rotation {int(np.degrees(angle))} degres")
plt.axis("equal")
plt.legend()
plt.title("Une matrice fait tourner une figure")
plt.show()

angle_30 = np.pi / 6
angle_60 = np.pi / 3
angle_90 = np.pi / 2

R30 = rotation(angle_30)
R60 = rotation(angle_60)
R90 = rotation(angle_90)

R_combine = R60 @ R30

ecart = np.max(np.abs(R_combine - R90))
print("Écart maximal entre R(60) @ R(30) et R(90) :", ecart)
print("Vérification valide :", ecart < 1e-12)

#Exercice 7.1

import numpy as np


def determinant(A, tolerance=1e-14):
    n = len(A)
    M = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(A[i][j])
        M.append(ligne)
        
    det = 1.0
    echanges = 0
    
    for k in range(n):
        meilleure = k
        valeur_max = abs(M[k][k])
        for i in range(k + 1, n):
            if abs(M[i][k]) > valeur_max:
                valeur_max = abs(M[i][k])
                meilleure = i
                
        if abs(M[meilleure][k]) <= tolerance:
            return 0.0
            
        if meilleure != k:
            temp = M[k]
            M[k] = M[meilleure]
            M[meilleure] = temp
            echanges = echanges + 1
            
        det = det * M[k][k]
        
        for i in range(k + 1, n):
            facteur = M[i][k] / M[k][k]
            for j in range(k, n):
                M[i][j] = M[i][j] - facteur * M[k][j]
                
    if echanges % 2 == 1:
        det = -det
        
    return det


A1 = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]
A2 = [[1, 2], [2, 4]]

print(determinant(A), float(np.linalg.det(np.array(A, dtype=float))))
print(determinant([[1, 2], [2, 4]]))

#Exercice 8.1
from fractions import Fraction

def generer_hilbert(n):
    matrice = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(Fraction(1, i + j + 1))
        matrice.append(ligne)
    return matrice

taille = 12
H = generer_hilbert(taille)

b = []
for ligne in H:
    somme_ligne = sum(ligne)
    b.append(somme_ligne)

try:
    resoudre(H, b)
except ValueError as err:
    print("Premier essai :", err)

x = resoudre(H, b, tolerance=0)
print("Résultat exact :", x)

verification = []
for v in x:
    verification.append(v == 1)

print(all(verification))

#Exercice 9.1

import numpy as np

def translation(x, y):
    return np.array([[1.0, 0.0, x],[0.0, 1.0, y],[0.0, 0.0, 1.0]])

def rotation(angle):
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([[c, -s, 0.0],[s,  c, 0.0],[0.0, 0.0, 1.0]])

point = np.array([1.0, 0.0, 1.0])

t = translation(3, 1)
r = rotation(np.pi / 2)

res_1 = r.dot(t.dot(point))
print("1.", np.round(res_1, 10))


res_2 = t.dot(r.dot(point))
print("2.", np.round(res_2, 10))
