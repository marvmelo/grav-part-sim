import numpy as np

class Vec2D():

    def __init__(self, x, y):

        self.coords = np.array((x,y))

    def __add__(self, o):

        return self.coords + o.coords

    def __sub__(self, o):

        return self.coords - o.coords

    def __rmul__(self, o):

        return o*self.coords

    def getlength(self):

        return ((self.coords[0]**2)+(self.coords[2])**2)**(1/2)

class Part():

    def __init__(self, p, v, m=1, c=0):

        self.position = p
        self.velocity = v
        self.mass = m
        self.charge = c

    
