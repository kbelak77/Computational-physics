import projectile_drag as pro
import matplotlib.pyplot as plt
list_t = [0.1, 0.01, 0.001]
#P1= pro.Projectile(0,0,20,50, 0, 0, 0, 50)
#a, b = P1.kosi_hitac()
list_x = []
list_y = []
for el in list_t:
    P = pro.Projectile(0,0,20, 60, 1.5, 0.7, 5, 50, el)
    c,d = P.kosi_hitac() #x, y
    list_x.append(c)
    list_y.append(d)
txt = 'Euler {}'
for i in range(len(list_t)):
    c = list_t[i]
    plt.plot(list_x[i], list_y[i], lw = 0.5, label = txt.format(c))


P2 = pro.Projectile(0,0,20, 60, 1.5, 0.7, 5, 50, 0.01)
s, z = P2.move_R()

plt.ylabel('y[m]')
plt.xlabel('x[m]')
plt.plot(s, z, lw = 0.5, label = 'Runge-Kutta 0.01')
plt.legend(loc = 'lower right')
plt.show()
