import numerical_calculus as cal
import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return 5*x**3 - 2*x**2 + 2*x - 3
def f2(x):
    return np.cos(x)
def f3(x):
    return 2*(x**2) + 3
def f1_d(x):
    return 15*(x**2) - 4*x + 2
def f2_d(x):
    return (-1)*np.sin(x)

#provjera - trigonometrijska funkcija
#print(cal.derivacija(f2, np.pi/2, 0.001, 1))
#print(f2_d(np.pi/2))
#provjera - kubna funckcija
#print(cal.derivacija(f1, 5, 0.001, 1))
#print(f1_d(5))

a, b = cal.raspon(f1, -2, 2, 0.1)
c, d = cal.raspon(f1, -2, 2, 0.01)
x_list = [x for x in np.arange(-2, 2, 0.01)]
plt.scatter(b, a, s = 5, c = 'blue')
plt.scatter(d, c, s = 1)
plt.plot(x_list, f1_d(np.array(x_list)), c = 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Numerička derivacija')
plt.show()

#Testirajte modul na primjeru proizvoljno odabrane funkcije i raspona integracije. Neka korisnik u svom
#kodu importa modul calculus i za integraciju koristi gotove metode iz tog modula. Nacrtajte na istom grafu
#analitičko riješenje i numerička riješenja za različiti broj koraka i obe metode numeričke integracije.

go = []
do = []
tz= []
Ns = []
for N in range(100, 900, 50):
    Ns.append(N)
    t = cal.trapezna(f3, 0, 1, N)
    x, y = cal.integracija(f3, 0, 1, N)
    do.append(x)
    go.append(y)
    tz.append(t)


y = np.ones((900, 1))*11/3
plt.plot(y)
plt.scatter(Ns, go, s = 3)
plt.scatter(Ns, do, s = 3)
plt.scatter(Ns, tz, s = 3)
plt.title('Numerička integracija')
plt.ylabel('Integral')
plt.xlabel('N koraka')
plt.show()


