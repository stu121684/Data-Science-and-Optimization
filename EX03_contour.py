import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker, cm

origin = 'lower'

delta = 0.0625
levels = 500
x = y = np.arange(-0.5, 2, delta)
X, Y = np.meshgrid(x,y)
Z1 = 100.0 * (Y - X**2)**2 + (1 - X)**2

norm1=cm.colors.Normalize(vmax=abs(Z1).max(),vmin=-abs(Z1).max())
fig1, ax1 = plt.subplots(constrained_layout=True)
CS1 = ax1.contour(X, Y, Z1, levels, norm=norm1)
ax1.scatter(1,1,marker="x",c="black")
fig1.colorbar(CS1)

x2 = y2 = np.arange(-3, 7, delta)
X2, Y2 = np.meshgrid(x2,y2)
Z2 = (X2-2)**4 + (X2-2*Y2)**2
norm2=cm.colors.Normalize(vmax=abs(Z2).max(),vmin=-abs(Z2).max())
fig2,ax2 = plt.subplots(constrained_layout=True)
CS2 = ax2.contour(X2,Y2,Z2, levels, norm=norm2)
ax2.scatter(2,1,marker="x",c="black")
fig2.colorbar(CS2)

plt.show()
