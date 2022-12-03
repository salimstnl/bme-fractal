dbase = np.array([
    [0, 1], 
    [0, 0]
    ])


def df1(cylinder):
    x = cylinder[0]*1/2 - cylinder[1]*1/2
    y = cylinder[0]*1/2 + cylinder[1]*1/2

    return np.array([x, y])


def df2(cylinder):
    x = - cylinder[0]*1/2 - cylinder[1]*1/2 + 1
    y = cylinder[0]*1/2 - cylinder[1]*1/2

    return np.array([x, y])


def dragon(base, n):
    if n == 0:
        return base
    
    x = np.array([])
    y = np.array([])
    x = np.append(x, [df1(base)[0], df2(base)[0]])
    y = np.append(y, [df1(base)[1], df2(base)[1]])

    return dragon([x,y], n-1)


def dplot(base, n=4):
    plt.figure(figsize=[7.2, n*2.7])
    
    for k in range(n):
        fractal = dragon(base, k)
        x = fractal[0]
        y = fractal[1]
        
        plt.subplot(n, 2, k+1)
        plt.title(f"level {k}")
        plt.xticks([])
        plt.yticks([])
        for i in range(0,len(x), 2):
            plt.plot(x[i:i+2], y[i:i+2], "indigo")
            
    plt.show()
