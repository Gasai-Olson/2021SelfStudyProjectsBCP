import matplotlib.pyplot as plt
import numpy as np

def write(arg):
    f = open('/Users/timyc1/Desktop/houseofrep/Output.txt','w') 
    f.write(arg)

def calculate(arg):
    write(str(eval(str(arg))))

def graph(arg):
    x = np.array(range(100))
    y = eval(arg)

    # Create the plot
    plt.plot(x,y)

    # Show the plot
    plt.show()

