kbase = np.array([
    [0, 1], 
    [0, 0]
    ])


def kf1(cylinder):
    x = cylinder[0]*1/3
    y = cylinder[1]*1/3

    return np.array([x, y])


def kf2(cylinder):
    x = (cylinder[0]*1/2 - cylinder[1]*math.sqrt(3)/2)*1/3 + 1/3
    y = (cylinder[1]*1/2 + cylinder[0]*math.sqrt(3)/2)*1/3

    return np.array([x, y])


def kf3(cylinder):
    x = (cylinder[0]*1/2 + cylinder[1]*math.sqrt(3)/2)*1/3 + 1/2
    y = (cylinder[1]*1/2 - cylinder[0]*math.sqrt(3)/2)*1/3 + math.sqrt(3)/6

    return np.array([x, y])


def kf4(cylinder):
    x = cylinder[0]*1/3 + 2/3
    y = cylinder[1]*1/3

    return np.array([x, y])


def koch(base, n):
    if n == 0:
        return base
    
    x = np.array([])
    y = np.array([])
    x = np.append(x, [kf1(base)[0], kf2(base)[0], kf3(base)[0], kf4(base)[0]])
    y = np.append(y, [kf1(base)[1], kf2(base)[1], kf3(base)[1], kf4(base)[1]])

    return koch([x,y], n-1)


def cplot(base, n=4):
    plt.figure(figsize=[7.2, n*2.7])
    
    for k in range(n):
        fractal = koch(base, k)
        x = fractal[0]
        y = fractal[1]
        
        plt.subplot(n, 1, k+1)
        plt.title(f"level {k}")
        plt.xticks([])
        plt.yticks([])
        for i in range(0,len(x), 4):
            plt.plot(x[i:i+4], y[i:i+4], "indigo")
            
    plt.show()
