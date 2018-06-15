import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return 2*x+1

x=np.linspace(1,5,100)
y=np.array([f(a) for a in x])

above = [b+np.random.random_integers(1,100)/10.0+np.random.sample() for b in y]
below = [b-np.random.random_integers(1,100)/10.0-np.random.sample() for b in y]

plt.plot(x, y, linewidth=2)
plt.scatter(x, above, c="orange",marker="v")
plt.scatter(x, below, c="g")
axes = plt.gca()
axes.set_xlim([1,5])
axes.set_ylim([3,11])

plt.show()