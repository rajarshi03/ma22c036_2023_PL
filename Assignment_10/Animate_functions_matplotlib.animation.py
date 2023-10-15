import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the function f(x, t)
def f(x, t):
    return ((x + t) ** 2)/2 + 2 * np.sin(10 * (x - t))

# initializing a figure in 
# which the graph will be plotted 
fig = plt.figure() 

# marking the x-axis and y-axis 
axis = plt.axes(xlim =(0, 10), ylim =(-2, 50)) 

# initializing a line variable 
line, = axis.plot([], [], lw =1) 

# data which the line will 
# contain (x, y) 
def init(): 
    line.set_data([], []) 
    return line,

def animate(t): 
    x = np.linspace(0, 10, 1000) 

    # plots a sine graph 
    y = f(x,t)
    line.set_data(x, y)
    return line, 

anim = FuncAnimation(fig, animate, 
                    init_func = init, 
                    frames = 200, 
                    interval = 200, 
                    blit = True)

plt.show()
