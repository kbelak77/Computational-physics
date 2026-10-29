import numpy as np
import matplotlib.pyplot as plt

class Planet:
    def __init__(self,r1, r2, v1, v2, m1, m2, t):
        self.r1 = np.array(r1)
        self.r2 = np.array(r2)
        self.v1 = np.array(v1)
        self.v2 = np.array(v2)
        self.t = t
        self.m1 = m1
        self.m2 = m2
        self.dt = 1/self.t
        self.G = 6.67408 * 10**(-11)
        self.list_r1 = []
        self.list_r2= []

    def __move(self):
        self.dt = self.dt * 24*3600
        self.dr = np.linalg.norm(self.r2-self.r1)
        self.a1 = - self.G * self.m2 * (self.r1-self.r2)/(self.dr**3)
        self.v1 = self.v1 + self.a1*self.dt
        self.r1 = self.r1 + self.v1*self.dt

        self.dr = np.linalg.norm(self.r2-self.r1)

        self.a2 = - self.G * self.m1 * (self.r2-self.r1)/(self.dr**3)
        self.v2 = self.v2 + self.a2*self.dt
        self.r2 = self.r2 + self.v2*self.dt
        self.dt = self.dt/(24*3600)

    def Motion(self):
        self.t0 = 0.
        while self.t0<=self.t:
            self.__move()
            self.t0+=self.dt
            self.list_r1.append(self.r1)
            self.list_r2.append(self.r2)
    
        return self.list_r1, self.list_r2