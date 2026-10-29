#Napišite program koji crta putanju nabijene čestice u konstantnom električnom i magnetnom polju. 
#Demonstrirajte valjanost putanje za slučaj nabijene čestice koja se giba u konstatnom magnetnom polju B⃗ = (0, 0, B)
#i ima sve tri komponente početne brzine različite od 0. Kako se u tom slučaju giba elektron, a kako pozitron?

import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,r, v, t, m, q, E, B, dt= 0.01):
        self.r = np.array(r)
        self.v = np.array(v)
        self.t = t
        self.m = m
        self.q = q
        self.E = E
        self.B = B
        self.dt = dt
        self.list_r = []

    def __move(self):
        self.a = (self.q/self.m)*(self.E + np.cross(self.v, self.B))
        self.v = self.v + self.a*self.dt
        self.r = self.r + self.v*self.dt

    def Motion(self):
        self.t0=0
        while self.t0<=self.t:
            self.__move()
            self.t0+=self.dt
            self.list_r.append(self.r)
        return self.list_r


    