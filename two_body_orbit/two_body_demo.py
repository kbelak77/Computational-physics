import two_body as C
import matplotlib.pyplot as plt
import numpy as np

r1 = (0,0)
r2 = ((1.486) * 10**11, 0)
v1 = (0,0)
v2 = (0, 29783)
Ms = (1.989)*10**30
Mz = (5.9742)*10**24
Set_1 = C.Planet(r1, r2, v1, v2, Ms, Mz, 365.242)

Put_1, Put_2 = Set_1.Motion()
Put_1 = np.asarray(Put_1)
Put_2 = np.asarray(Put_2)

plt.plot(Put_1[:, 0], Put_1[:, 1], label = 'Sunce', c = 'orange')
plt.plot(Put_2[:, 0], Put_2[:, 1], label = 'Zemlja', c = 'blue')
plt.title('Sistem Sunce-Zemlja')
plt.axis('scaled')
plt.legend(loc = 'lower right')
plt.show()