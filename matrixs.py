import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

# Domain 30x30 (at least)
# 3 species (at least) - empty can count as one species/elements
# You need to plot the 2D domain and the number of elements over the 100 iterations
# 100 iterations (at least)

# matrix states: asymptomatic(0), affected(1), recovery(2)
"""
# update the states (etc asymptomatic, affected, recovery) based on neighborhood
def updateStates(#code here):
    #code here

# update the position (aka the neighborhood and moving the recovery)
def updatePositions(#code here):
    #code here
"""

# plots grid graph
def plotSpatial(data, fileNum):
    colormap = colors.ListedColormap(['white','blue','red'])
    plt.figure(figsize=(7,6))
    plt.pcolor(data, cmap=colormap, edgecolors='k', linewidths=1, vmin=0,vmax=2)
    cbar = plt.colorbar(label="", orientation="vertical", ticks=[0.33,1,1.66])
    cbar.ax.set_yticklabels(['No symptoms', 'Affected', 'Recovering'])
    plt.imshow(data)
    plt.show()
    plt.savefig('figure_' + str(fileNum) + '.jpg', bbox_inches='tight', pad_inches=0.02)
    plt.close()


def main():
    # initial random matrix
    random.seed(time.time())
    currTime = 0
    sizeX, sizeY = 30, 30
    domain = np.array([random.randint(0, 2) for x in range(sizeX*sizeY)]).reshape(sizeY,sizeX)
    print(domain)

    # plots initial matrix
    plotSpatial(domain, currTime)

    # adds values
    simTime, asymptomatic, affected, recovery = [], [], [], []
    simTime.append(currTime)
    asymptomatic.append(np.count_nonzero(domain == 0))
    affected.append(np.count_nonzero(domain == 1))
    recovery.append(np.count_nonzero(domain ==2))

    # for loop for 100 iterations
    for currTime in range(1, 101):
        print(currTime)
    # code here
    
main()