import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
# or ax = fig.gca(projection='3d')

# line/scatter plot : x,y,z는 1차원 배열 
ax.plot(1,2,3)  
ax.scatter(4,5,6)
'''
# surface, wireframe plot : X,Y,Z는 2차원 배열
ax.plot_surface(X,Y,Z,...)
ax.plot_wireframe(X,Y,Z,...)

# bar3d plot : x, y, z는 1차원 배열
ax.bar3d(x,y,width,depth,z,...)
'''