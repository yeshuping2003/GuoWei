# simpleStudyplot1.py
import numpy as np
import matplotlib.pyplot as plt
import math

def simple_line_plot(x, y, figure_no):
    plt.figure(figure_no)
    plt.plot(x, y)
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Simple Line')

if __name__ == "__main__":
    plt.close('all')

    x = np.arange(1,100,dtype = float)

    y = np.array([np.power(math.log(xx), 2) for xx in x])
    
    figure_no = 1
    simple_line_plot(x, y, figure_no)


    #plt.show()

    x = np.arange(1,100,dtype = float)

    y = np.array([np.power(xx, 2) for xx in x])
    
    figure_no = 2
    simple_line_plot(x, y, figure_no)


    plt.show()

