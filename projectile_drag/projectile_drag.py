#Napišite kod koji sadrži klasu Projectile koja ima implementirane metode za simuliranje kosog hitca u dvije
#dimenzije s otporom zraka. Testirajte za koji korak ∆t Euler-ova metoda daje dovoljno precizno numeričko
#rješenje koje na x − y grafu nema naznake ne-fizikalnog gibanja
import math
import numpy as np

class Projectile:
    def __init__(self, x, y, v, kut, rho, Cd, A, m, dt= 0.01):
        self.x = x
        self.dt = dt
        self.y = y
        self.v = v
        self.m = m
        self.kut= np.radians(kut)
        self.vx = v * np.cos(self.kut)
        self.vy = v * np.sin(self.kut)
        self.g = -9.81
        self.rho = rho
        self.Cd = Cd
        self.A = A
        self.xs = [x]
        self.ys = [y]

    def __move(self): 
        self.ax = (-1)*np.sign(self.vx)*((self.rho * self.Cd * self.A)/(2*self.m))*(self.vx**2)
        self.ay = self.g + (-1)*np.sign(self.vy)*((self.rho * self.Cd * self.A)/(2*self.m))*(self.vy**2)
        self.vx += self.ax * self.dt
        self.vy += self.ay*self.dt
        self.x += self.vx*self.dt
        self.y += self.vy*self.dt
        self.xs.append(self.x)
        self.ys.append(self.y)


    def kosi_hitac(self): 
        self.y = self.y
        while self.y>=0:
            self.__move()
        return self.xs, self.ys
    
    
    def Runge(self):
       self.B = (self.rho*self.Cd*self.A)/(2*self.m)

       self.k1vx = (-np.sign(self.vx)*self.B*(self.vx**2))*self.dt
       self.k1x = self.vx * self.dt
       self.k2vx = (-np.sign(self.vx + self.k1vx/2)*self.B*((self.vx+self.k1vx/2)**2)) * self.dt
       self.k2x = (self.vx + self.k1vx/2)*self.dt
       self.k3vx = (-np.sign(self.vx + self.k2vx/2)*self.B*((self.vx + self.k2vx/2)**2))* self.dt
       self.k3x = (self.vx + self.k2vx/2)* self.dt
       self.k4vx = (-np.sign(self.vx + self.k3vx)*self.B*((self.vx+self.k3vx)**2)) * self.dt
       self.k4x = (self.vx + self.k3vx)*self.dt

       self.vx += (1/6)*(self.k1vx + 2*self.k2vx + 2*self.k3vx + self.k4vx)
       self.x += (1/6)*(self.k1x + 2*self.k2x + 2*self.k3x + self.k4x)

       self.k1vy = (self.g -np.sign(self.vy)*self.B*(self.vy**2))*self.dt
       self.k1y = self.vy * self.dt
       self.k2vy = (self.g -np.sign(self.vy + self.k1vy/2)*self.B*((self.vy+self.k1vy/2)**2)) * self.dt
       self.k2y = (self.vy + self.k1vy/2)*self.dt
       self.k3vy = (self.g -np.sign(self.vy+ self.k2vy/2)*self.B*((self.vy + self.k2vy/2)**2))* self.dt
       self.k3y = (self.vy + self.k2vy/2)* self.dt
       self.k4vy = (self.g -np.sign(self.vy + self.k3vy)*self.B*((self.vy+self.k3vy)**2)) * self.dt
       self.k4y = (self.vy + self.k3vy)*self.dt

       self.vy += (1/6)*(self.k1vy + 2*self.k2vy + 2*self.k3vy + self.k4vy)
       self.y += (1/6)*(self.k1y + 2*self.k2y + 2*self.k3y + self.k4y)

    def move_R(self):
        self.list_x1 = []
        self.list_y1 = []
        while self.y >=0:
            self.list_x1.append(self.x)
            self.list_y1.append(self.y)
            self.Runge()
        return self.list_x1, self.list_y1

