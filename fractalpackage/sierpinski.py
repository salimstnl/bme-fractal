sbase = np.array([
    [0, 1/2, 1], 
    [0, math.sqrt(3)/2, 0]
    ])


def sf1(cylinder):
    """
    """
    x = cylinder[0]*1/2
    y = cylinder[1]*1/2
    
    return np.array([x, y])


def sf2(cylinder):
    x = cylinder[0]*1/2 + 1/4
    y = cylinder[1]*1/2 + math.sqrt(3)/4
    
    return np.array([x, y])


def sf3(cylinder):
    x = cylinder[0]*1/2 + 1/2
    y = cylinder[1]*1/2
    
    return np.array([x, y])


def sierpinski(base, n):
    if n == 0:
        return base
      
    x = np.array([])
    y = np.array([])
    x = np.append(x, [sf1(base)[0], sf2(base)[0], sf3(base)[0]])
    y = np.append(y, [sf1(base)[1], sf2(base)[1], sf3(base)[1]])
    
    return sierpinski([x,y], n-1)


def splot(base, n=4):
    plt.figure(figsize=[7.2, n*3.6])
    for k in range(n):
        fractal = sierpinski(base, k)
        x = fractal[0]
        y = fractal[1]
        
        plt.subplot(n, 2, k+1)
        plt.title(f"level {k}")
        plt.xticks([])
        plt.yticks([])
        for i in range(0,len(x), 3):
            plt.fill(x[i:i+3], y[i:i+3], "indigo")
            
    plt.show()
