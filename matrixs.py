import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

# Domain 30x30 (at least)
# 3 species (at least) - empty can count as one species/elements
# You need to plot the 2D domain and the number of elements over the 100 iterations
# 100 iterations (at least)

# matrix states: empty(0), affected(1), recovery(2)
"""
arr = np.random.random((30,30))
print(arr)

H = np.array([[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]])

plt.imshow(arr, interpolation='none')
plt.show()
"""
def plotSpatial(data, fileNum):
    colormap = colors.ListedColormap(['gray','blue','red'])
    plt.figure(figsize=(7,6))
    plt.pcolor(data, cmap=colormap, edgecolors='k', linewidths=1, vmin=0,vmax=2)
    cbar = plt.colorbar(label="", orientation="vertical", ticks=[0.33,1,1.66])
    cbar.ax.set_yticklabels(['No symptoms', 'Affected', 'Recovering'])
    plt.imshow(data)
    plt.savefig('figure_' + str(fileNum) + '.jpg', bbox_inches='tight', pad_inches=0.02)
    plt.close()
    plt.grid()


def main():
    random.seed(time.time())
    currTime = 0
    sizeX, sizeY = 30, 30
    domain = np.array([random.randint(0, 2) for x in range(sizeX*sizeY)]).reshape(sizeY,sizeX)
    print(domain)
    # plotSpatial(domain, currTime)
    plt.imshow(domain, interpolation='none')
    plt.show()


main()