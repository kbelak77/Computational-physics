import numpy as np
import math as m
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numerical_calculus as cal

#def f(x):
    #return 4/(1 + x**2)

#print('Trapezna:', cal.trapezna_integracija(f, 0, 4, 5), 'Simpson:',cal.Simpson(f, 0, 4, 5), 'Gauss:', cal.Gauss_int(f,0,4,5))

m = 3.37*10**(-26)
T=300 
Vg = 559.4 + 50
Vd = 559.4 - 50
kb = 1.38064852*10**(-23)
k = np.sqrt((m/(2*np.pi*kb*T))**3) * 4*np.pi

def fja(v):
    return (v**2)* np.exp(-(m*v**2)/(2*kb*T))
trapezna = []
simpsonova = []
gauss = []
ms = [10, 50, 100]
for el in ms:
    trapezna.append(k*cal.trapezna(fja, Vd, Vg, el))
    simpsonova.append(k*cal.Simpson(fja, Vd, Vg, el))
    gauss.append(k*cal.Gauss_int(fja, Vd, Vg, el))

podaci = { 'm': ms,
            'Trapezna': trapezna,
            'Simpsonova': simpsonova,
            'Gaussova': gauss
}

df = pd.DataFrame(podaci)
pd.options.display.float_format = "{:.10f}".format
with open ('maxwell_boltzmann_results.txt', 'w') as f:
    f.write(df.to_string(index=False))
