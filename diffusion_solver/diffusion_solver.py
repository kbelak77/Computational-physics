import numpy as np
import math as m
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#definiramo vrij u t=0

L= 20 #domena prostora
b= 10**(-2)
Nx = 100
Nt = 500
dx = (L)/(Nx - 1)
dt = 0.5


alpha = b * (dt/(dx**2))
if alpha >=(1/2):
    print('Rješenje nije stabilno za ovaj odabir dt.')
#rubni uvjeti su a=b=0

#funkcija je dvodimenz polje, u prvom redku postavljamo vrijednosti x-a za t=0 kako je zadano

#ja u biti postavljam vrijednosti u funkciju za odredeni t odnosno x kad mmi je poznat iznos funkcije, matrica je u biti pohrana vrijednosti funkcije za dana cvorista
#potrebna je matr za pohranu tih podataka a pristupam njenim elementima u petlji za rekurzivno racunati iznose funkcije za sve x odn t
#svaki redak je "slika" fje u vremenu t
#stupac u prostoru x
#poznajemo vrij za xeve, trazimo vrij u vremenskoj evoluciji koristeci formulu
#definiramo domene za t odn x

x = np.linspace(0, L , Nx) #u Nx cvorova na ovoj domeni racunamo
t = np.linspace(0, Nt*dt, Nt) #T=Nt*dt je finalno vrijeme
fja = np.zeros((Nt, Nx))
#redak= nulti za poc uvjete odn t=0

for k in range(len(x)): #za t=0 odn pocetne uvjete pridodaje vrijednosti fje koje su zadane, a ovisne o x
    if (x[k] >= 2) and (x[k] <= 5):
        fja[0, k] = 5.5
    else:
        fja[0,k] = 0.0
fja2 = fja.copy()
fja3=fja.copy()
#u matricu fje ne upisujem listu xeva odn t jer to nije lista toga vec poznate vrijednosti fje
#u tim tockama koje poznajemo

#EKSPLICITNA
#rekurzivno popunjavanje iznosa funkcije prema formuli uz pomoc poznatih p.u., r.u.
for j in range(0, Nt-1): #radi se o indeksaciji pa krece od nula bit ce viska
    for i in range(1, Nx-1): #krece od x=1 jer je nula za x=0 i za x=20 sto je posljednji clan u x
        fja[j+1, i] = alpha*fja[j, i+1] + (1-2*alpha)*fja[j, i] + alpha*fja[j, i-1]
#iz rubnih uv
#print(fja2)

#Implicitno ovaj mora matrično? ispunjen je uvjet a=b=0
#V je stupčasta matrica sa vrijednostima funkcije u istom vremenu ali varijabilnim prostornim koord
#odnosno Vj je jedan stupac što nosi vrijednosti matrice u vrem trenutku/koraku j
#doznajemo sve vrij za sve t rješavajući rekurz
#obje umanjene za 2 zbog elimin p.u.

#IMPLICITNA
A = np.zeros((Nx - 2, Nx - 2))
np.fill_diagonal(A, 1 + 2 * alpha) #popunjavanje matr prema sabloni
np.fill_diagonal(A[1:], -alpha)
np.fill_diagonal(A[:, 1:], -alpha)

#print(A)
#fja2
#indeksacija
#Nepoznanica je Vj+1 B = Vj-1

#THOMASOV ALGORITAM
def Thomas(matrica, d):
    Ci_ii = [matrica[0, 1] / matrica[0, 0]]  # C1
    Di_ii = [d[0] / matrica[0, 0]]           # D1


    for i in range(1, len(matrica) - 1):
        ci = matrica[i][i + 1] #c2'' nadalje
        bi = matrica[i][i] #el na dijagonali
        ai = matrica[i+1][i] #el za jedan ispod dijag #Koristimo ih za daljnji izracun al ih se rjesavamo
        di = d[i]
        
        ci_ii = ci / (bi - ai * Ci_ii[i - 1]) #Formula za ci''
        di_ii = (di - ai * Di_ii[i - 1]) / (bi - ai * Ci_ii[i - 1])
        
        Ci_ii.append(ci_ii) #Matrice koje imaju samo ove probrane el
        Di_ii.append(di_ii)

    Di_ii.append((d[-1] - matrica[-1, -2] * Di_ii[-1]) / (matrica[-1, -1] - matrica[-1, -2] * Ci_ii[-1]))
    Ci_ii.append(0) 

    #Ručno ubacivanje
    X = np.zeros(len(matrica))
    X[-1] = Di_ii[-1]  
 
    for i in range(len(matrica) - 2, -1, -1):
        X[i] = Di_ii[i] - Ci_ii[i] * X[i + 1] 

    return X


for ii in range(0, Nt-1):
     #pristupa n-tom redku matrice;vrijeme
     #V je matrica sa elementima iz spec redka za spec t(fiksan t)?
    #V_j = fja2[ii+1, 1:-1] #bez prvog i zadnjeg clana jer su ionako nula za t=0 i t=T
    #Vj-1 = A*Vj da nerac inverz
    fja2[ii+1, 1:-1] = Thomas(A, fja2[ii, 1:-1])
    #fja2[ii, 1:-1] = np.linalg.solve(A, V_j) #rac iz prethodnog iduci


#CRANK-NICOLSONOVA
#fja3
B = np.zeros((Nx - 2, Nx - 2))
np.fill_diagonal(B, 2) #popunjavanje matr prema sabloni
np.fill_diagonal(B[1:], -1)
np.fill_diagonal(B[:, 1:], -1)

for iii in range(0, Nt-1):
    V_jp = np.dot((np.eye(Nx-2) - (alpha/2)*B), fja3[iii, 1:-1]) #prosli
    #fja3[iii+1, 1:-1] = np.linalg.solve(A,V_jp)
    fja3[iii+1, 1:-1] = Thomas((np.eye(Nx-2) + (alpha/2)*B), V_jp)



js = [f for f in range(0,500, 100)]
#print(js)
#traži graf fje i x/dx
plt.figure(figsize=(12, 6))
for el in js:
    plt.plot(x/dx, fja[el], label=f"Eksplicitna t={el * dt}s")
    plt.plot(x/dx, fja2[el], '.', label=f"Implicitna t={el * dt}s")
    plt.plot(x/dx, fja3[el], '--', label=f"Crank-Nicolsonova t={el * dt}s")

plt.xlabel("x/dx")
plt.ylabel("ρ (kg/m)")
plt.legend()
plt.show()