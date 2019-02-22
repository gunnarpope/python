import matplotlib.pyplot as plt

def plot(x,y, **kwargs):

    plt.figure(dpi=300)
    plt.plot(x,y)
    plt.grid(True)
    
    for key, value in kwargs.items():
        if key == 'title':
            plt.title(value)
        if key == 'xlabel':
            plt.xlabel(value)
        if key == 'ylabel':
            plt.ylabel(value)
        if key == 'xlim':
            plt.xlim(value)
        if key == 'ylim':
            plt.ylim(value)
        if key == 'grid':
            plt.ylim(value)

            
    plt.show()
    

if __name__ == '__main__':
    
    x = range(10)  
    y = [ 2**c for c in x]

    plot(x,y)
    plot(x,y, xlabel='time (min)', ylabel='height (m)', title='Time vs Height')
    
