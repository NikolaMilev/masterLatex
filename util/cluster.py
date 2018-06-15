import numpy as np
import matplotlib.pyplot as plt
r=0.07
np.random.seed(6)
sigma=0.1
mu=1
cluster1=0.2*np.random.randn(2,7)+0.6
center1=(np.sum(cluster1[0])/7.0, np.sum(cluster1[1])/7.0)
rad1 = np.sqrt(np.max(np.multiply(cluster1[0]-center1[0], cluster1[0]-center1[0]) + np.multiply(cluster1[1]-center1[1], cluster1[1]-center1[1])))
circle1=plt.Circle(center1, rad1+r, color="g", fill=False, linewidth=1, linestyle="dashed")
print rad1

cluster2=0.3*np.random.randn(2,11)+1.3
cluster2[1]-=2
center2=(np.sum(cluster2[0])/11.0, np.sum(cluster2[1])/11.0)
rad2 = np.sqrt(np.max(np.multiply(cluster2[0]-center2[0], cluster2[0]-center2[0]) + np.multiply(cluster2[1]-center2[1], cluster2[1]-center2[1])))
circle2=plt.Circle(center2, rad2+r, color="r", fill=False, linewidth=1, linestyle="dashed")


cluster3=0.15*np.random.randn(2,20)-1
center3=(np.sum(cluster3[0])/20.0, np.sum(cluster3[1])/20.0)
rad3 = np.sqrt(np.max(np.multiply(cluster3[0]-center3[0], cluster3[0]-center3[0]) + np.multiply(cluster3[1]-center3[1], cluster3[1]-center3[1])))
circle3=plt.Circle(center3, rad3+r, color="b", fill=False, linewidth=1, linestyle="dashed")
#print center1, center2, center3

fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(cluster1[0],cluster1[1], c="green")
ax.add_artist(circle1)
scatter = ax.scatter(cluster2[0],cluster2[1], c="red")
ax.add_artist(circle2)
scatter = ax.scatter(cluster3[0],cluster3[1], c="blue")
ax.add_artist(circle3)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.ylabel('y').set_rotation(0)
ax.set_aspect(1)
ax.set_xlim(-2,2.1)
ax.set_ylim(-2,1.5)
# x = np.random.randn(10)
#print x
# y = np.random.randn(10)
# Cluster = np.array([0, 1, 1, 1, 3, 2, 2, 3, 0, 2])    # Labels of cluster 0 to 3
# centers = np.random.randn(4, 2) 

# fig = plt.figure()
# ax = fig.add_subplot(111)
# scatter = ax.scatter(x,y,c=Cluster,s=50)
# for i,j in centers:
#     ax.scatter(i,j,s=50,c='red',marker='+')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# plt.colorbar(scatter)

plt.show()