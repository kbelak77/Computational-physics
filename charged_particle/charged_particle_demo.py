import charged_particle as Par
import numpy as np
import matplotlib.pyplot as plt

#Napišite program koji crta putanju nabijene čestice u konstantnom električnom i magnetnom polju. 
# Demonstrirajte valjanost putanje za slučaj nabijene čestice koja se giba u konstatnom magnetnom polju B⃗ = (0, 0, B)
#i ima sve tri komponente početne brzine različite od 0. Kako se u tom slučaju giba elektron, a kako pozitron

E = np.array((0, 0, 0))
B = np.array((0, 0, 1))
v = (0.1, 0.1, 0.1)
r = (0, 0, 0)

P1 = Par.Particle(r, v, 20, 1, 1, E, B)
P2 = Par.Particle(r, v, 20, 1, -1, E, B)

positions_p= np.array(P1.Motion())
positions_e= np.array(P2.Motion())

ax = plt.axes(projection='3d')
ax.plot(positions_p[:, 0], positions_p[:, 1], positions_p[:, 2], label = 'Pozitron')
ax.plot(positions_e[:, 0], positions_e[:, 1], positions_e[:, 2], label = 'Elektron') # sve elemente 1 stupc npr (x koord)
ax.view_init(18, 37)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend(loc = 'lower right')
plt.show()
