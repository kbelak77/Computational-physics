#Prva metoda kao ulazne parametre prima funkciju i točku, a kao rezultat vraća vrijednost derivacije funkcije u toj točki.
#Druga prima kao ulazne parametre funkciju i gornju i donju granicu raspona derivacije. Funkcija korisniku vraća listu točaka 
#u kojima će biti izvršena numerička derivacija na zadanom rasponu i iznose derivacije funkcije u tim istim točkama
import math
import numpy as np

def derivacija(fja, t, d, m=0):
    if m==1:
        return (fja(t+d)- fja(t))/d
    else:
        return (fja(t+d)- fja(t-d))/(2*d)

def raspon(fja, d, g, dx, m=0):
    derivacije=[]
    tocke=[]
    for i in np.arange(d, g, dx*5):
        der= derivacija(fja, i, dx, m)
        tocke.append(i)
        derivacije.append(der)
    return derivacije, tocke

# funkciju, granice integracije i broj podjela za numeričku integraciju

def integracija(fja, d, g, N):
    dx= (g-d)/N
    i = 0
    donja = 0
    gornja = 0
    while i < N: #izvrsavat ce se za onoliko koraka
        donja+= fja(d)*dx
        gornja+=fja(d+dx) * dx
        d+=dx
        i+=1
    return donja, gornja

def trapezna(fja, d, g, N):
    dx = (g-d)/N
    trapez=0
    i=0
    while i< N:
        trapez += (fja(d) + fja(d+dx))*(dx/2)
        d+=dx
        i+=1
    return trapez



def gauleg(x1, x2, n):
    
 #   Za zadanu donju i gornju granicu integracije x1 i x2, i stupanj polinoma na ova funkcija vraća listu x i w duljine n, koji sadrže nultočke 
 #   i težine za kvadratur Gauss-Legendre kvadraturu na zadanom intervalu.  
  
    EPS = 1e-14  # Preciznost 
    m = (n + 1) // 2 #jedna nultočka za nep n je nula, ostale simetrične--> tražimo pola nult
    #interval def lGR pol -1,1 --> pomocu ovog pozicioniramo nult LP na interval a,b
    #transf interval it -1,1 na a,b
    xm = 0.5 * (x2 + x1) #sredina int
    xl = 0.5 * (x2 - x1) #pola dulj int
    #da tocke na krajevima u int -1,1
    # Inicijalizacija
    #za zapis x,w
    x = np.zeros(n)
    w = np.zeros(n)
    #trazenje nultocaka fje z
    for i in range(1, m + 1): #jedno izvrsavanje jedna nultocka L polinoma
        z = math.cos(math.pi * (i - 0.25) / (n + 0.5)) #prva procjena nultocke, eksperimentalno određena forma
        while True: 
            p1 = 1.0 #za Legr polinom poc uvjet Legr. polinoma u pretpostavljenoj nultocki z mora dat 1
            p2 = 0.0 # nepostojeći--> zbog potreba rekurzije #vrijednost prethodnog polinoma #ALI nije stalno nula prolaskom kroz petlju poprima nenula vrijednosti; bitno samo incijalno da je nula

            for j in range(1, n + 1): #j+1 red l polinoma--> rekurzivno racunamo svaki prisutni red LP
                #rekurzivno racunanje polinoma
                p3 = p2
                p2 = p1
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j #Vrijednost trenutnog Lpn(z)
            pp = n * (z * p1 - p2) / (z * z - 1.0) #rekurz izr derivacija LPn(z)
            z1 = z #pohrana inicijalne pretp
            z = z1 - p1 / pp #nova pretpostavka nultočke NR METODA sad kad imamo L i der L
            if abs(z - z1) < EPS: #uvjet Newt-R metode
                break
        x[i - 1] = xm - xl * z #uz određenu jednu nultočku z za i-to izvrs petlje
        x[n - i] = xm + xl * z #posljednji
        w[i - 1] = 2.0 * xl / ((1.0 - z * z) * pp * pp) #tezine racunamo prema formuli
        w[n - i] = w[i - 1] #simetrija
    
    return x, w


def Simpson(fja, d, g, N):
    if N % 2 == 1:
        N += 1
    dx = (g-d)/N
    x = np.linspace(d, g, N+1)
    y = fja(x)
    return (dx/3)*(y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]) + y[-1])

def Gauss_int(fja, d, g, N):
    x, w = gauleg(d, g, N)
    return np.sum(w*fja(x))
