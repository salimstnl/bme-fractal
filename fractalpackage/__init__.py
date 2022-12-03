import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import itertools
import sympy
import math

plt.style.use('seaborn-dark')


class Fractal:
    """
    Class representing a self-similar set.
    """
  
    def __init__(self, x, y):
        """
        Initialize a Fractal object.
        
        Parameters:
            cylinder : List representing the cylinder(s) for the self-similar 
            set.
            ifs      : Tuple representing the iterated function systems of the 
            self-similar set.
            n        : Positive integer representing the level of iteration(s).
            (1 by default)
        """a
        self.x = x
        self.y = y
        
        
    def iterate(self):
        """
        Increase the cylinder level by one.
        """

      
    def plot(self):
        """
        Plot the fractal at the given level.
        """
