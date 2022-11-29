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

# update the states (etc asymptomatic, affected, recovery) based on neighborhood
def updateStates(domain,currTime):#code here
   movePosition(domain,xpos,ypos)
   display.clear_output(wait=True)
   display.display(plt.gcf())
   currTime.sleep(0.1)
   return




# update the position (aka the neighborhood)
#def updatePositions(#code here):
def movePosition (domain,xpos,ypos):
    direction= int(np.random.randint(0,2))

    if (direction ==0):
        ypos = ypos +1
    if (direction == 1):
        ypos= ypos -1
    if (direction ==2):
        xpos= xpos-1
    return domain[xpos][ypos]
    #code here



# plots grid graph
def plotSpatial(data, fileNum):
    colormap = colors.ListedColormap(['white', 'blue', 'red'])
    plt.figure(figsize=(10, 10))
    plt.pcolor(data, cmap=colormap, edgecolors='k', linewidths=1, vmin=0, vmax=2)
    cbar = plt.colorbar(label="", orientation="vertical", ticks=[0, 1, 2])
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
    domain = np.array([random.randint(0, 2) for x in range(sizeX * sizeY)]).reshape(sizeY, sizeX)
    print(domain)

    # plots initial matrix
    plotSpatial(domain, currTime)

    # adds values
    simTime, asymptomatic, affected, recovery = [], [], [], []
    simTime.append(currTime)
    asymptomatic.append(np.count_nonzero(domain == 0))
    affected.append(np.count_nonzero(domain == 1))
    recovery.append(np.count_nonzero(domain == 2))

    # for loop for 100 iterations
    for currTime in range(1, 101):
        simTime[currTime]
        simTime.append(currTime)
        affected.append[0]=308
        asymptomatic.append[0]=311
        recovery.append[0]=281

        print(currTime)
    # code here
    movePosition(domain,30,30)
    updateStates(domain,currTime)


