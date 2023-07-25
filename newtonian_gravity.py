#Classes for planets & universe.
import random
from matplotlib import pyplot as plt
import numpy as np

x_max = 100
y_max = 100
G = 1
dt = 0.1
N = 100

class System:
    """Solar system class to contain planets"""
    def __init__(self, fig = 0, ax = 0):
        self.planets = []
        self.N = N
        self.fig = fig
        self.ax = ax

    def initialise_axes(self):
        self.fig, self.ax= plt.subplots()
        self.fig.tight_layout()

    def addPlanet(self, planet):
        self.planets.append(planet)

    # def gravity(self):
    #     for i


class Planet:
    """Planet class to contain velocity etc."""
    def __init__(self, sys, mass = 1, position = [0,0], velocity = [0,0]):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def updatePosition(self):
        """Update (x,y) using simple Eulerian method of integration"""
        self.position = np.add(self.position, np.multiply(self.velocity, dt))

    def gravity(self, other):
        """Function to call calculation between 1 pair"""
        dx = self.position[0] - other.position[0]
        dy = self.position[1] - other.position[1]

        r = np.sqrt(dx**2 + dy**2)
