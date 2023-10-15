import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

# Define the function f(x, t)
def f(x, t):
    return ((x + t) ** 2)/2 + 2 * np.sin(10 * (x - t))


x=np.linspace(0,10,1000)

fig = plt.figure()
camera = Camera(fig)

for t in range(10):
    plt.plot(x,f(x,t))
    plt.annotate(f'Time = {t:.2f}', xy=(5, 3), fontsize=12)
    camera.snap()
animation = camera.animate()

plt.show()