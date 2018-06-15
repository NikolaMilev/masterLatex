import matplotlib.pyplot as plt 
import numpy as np

min_x=0
max_x=50

np.random.seed(5)

def f(x):
	retval = 1.5*x + 1 + np.random.random_sample(x.shape)*10
	retval[3] += 3
	retval[1] += 4
	return retval
x = np.linspace(min_x, max_x, 10)
y=f(x)

prava=np.poly1d(np.polyfit(x,y,1))
polinom=np.poly1d(np.polyfit(x,y,10))
print(y)
plt.scatter(x,y, s=80, c="g", edgecolors="g")
x=np.linspace(min_x, max_x)
y1=prava(x)
#plt.plot(x, y1, c="red", linewidth=2.5)
y2=polinom(x)
plt.plot(x,y2, c="red", linewidth=2.5)



plt.xlabel('x')
plt.ylabel('y')
plt.ylabel('y').set_rotation(0)
axes = plt.gca()

axes.set_xlim([min_x-0.4,max_x+0.2])
axes.set_ylim([np.min([np.min(y1),np.min(y1)])-0.4, np.max([np.max(y1),np.max(y1)])+0.4])

plt.show()
