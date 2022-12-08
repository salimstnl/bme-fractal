import matplotlib.pyplot as plt
import numpy as np
import math


cbase = np.array([
    [0, 1], 
    [0, 0]
    ])


def cf1(cylinder, a):
    x = cylinder[0]*(1-a)/2
    y = cylinder[1]

    return np.array([x, y])


def cf2(cylinder, a):
    x = cylinder[0]*(1-a)/2 + (1+a)/2
    y = cylinder[1]

    return np.array([x, y])


def cantor(base, n, a):
    if n == 0:
        return base
    
    x = np.array([])
    y = np.array([])
    x = np.append(x, [cf1(base, a)[0], cf2(base, a)[0]])
    y = np.append(y, [cf1(base, a)[1], cf2(base, a)[1]])

    return cantor([x,y], n-1, a)


def cplot(base, n=4, a=1/3):
    plt.figure(figsize=[7.2, n*1.8])
    
    for k in range(n):
        fractal = cantor(base, k, a)
        x = fractal[0]
        y = fractal[1]
        
        plt.subplot(n, 1, k+1)
        plt.title(f"level {k}")
        plt.xticks([])
        plt.yticks([])
        for i in range(0,len(x), 2):
            plt.plot(x[i:i+2], y[i:i+2], "indigo")
            
    plt.show()
