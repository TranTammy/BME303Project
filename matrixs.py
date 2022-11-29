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
"""


# update the position (aka the neighborhood and moving the recovery)
# affected: each day, if there is no recovering around, they have a 40% chance of becoming asymptomatic
# affected: each day, if there are asymptomatic around, they have a 30% chance of spreading covid
# recovering: the recovering individual has a 10% chance of dying
# recovering: the individual has a 50% chance of causing an affected person to be infected, replacing the affected person
def updateValues(data, fileNum):
    X = 901
    Y = 901
    neighbors = lambda x,y : [(x2,y2) for x2 in range(x-1,x+2) for y2 in range(y-1,y+2) if (-1 < x <= X and -1 < y <= Y and (x != x2 or y != y2) and (0 <= x2 <= X) and (0 <= y2 <= Y))]
    # enumerated iteration
    for idx, x in np.ndenumerate(data):
        # asymptomatic
        if x == 0:
            print()
        # affected
        elif x == 1:
            print()
            # rule 1
                #...
            # rule 2
                #...
        # recovery
        else:
            print()
            # rule 1
            r = random.random()
            if r < .1:
                data[idx] = 0
            #rule 2
                #...
    return data


# plots grid graph
def plotSpatial(data, fileNum):
    colormap = colors.ListedColormap(['white', 'blue', 'red'])
    plt.figure(figsize=(7, 6))
    plt.pcolor(data, cmap=colormap, edgecolors='k', linewidths=1, vmin=0, vmax=2)
    cbar = plt.colorbar(label="", orientation="vertical", ticks=[0.33, 1, 1.66])
    cbar.ax.set_yticklabels(['No symptoms', 'Affected', 'Recovering'])
    plt.savefig('figure_' + str(fileNum) + '.jpg', bbox_inches='tight', pad_inches=0.02)
    plt.close()


# plots line graph
def plotDynamics(data):
    fig, axes = plt.subplots(figsize=(7, 6))
    axes.plot(data[0], data[2], label='affected', color='blue')
    axes.plot(data[0], data[3], label='recovery', color='red')
    axes.set_xlabel('Time (days)')
    axes.set_ylabel('Number of individuals')
    axes.legend(bbox_to_anchor=(.3, 1), fontsize=13, fancybox=False, shadow=False, frameon=False)
    plt.imshow(data)
    plt.show()
    plt.savefig('temporalDynamics.pdf', bbox_inches='tight', pad_inches=0.02)
    plt.close()


def main():
    # initial random matrix
    random.seed(time.time())
    currTime = 0
    sizeX, sizeY = 30, 30
    domain = np.array([random.randint(0, 2) for x in range(sizeX * sizeY)]).reshape(sizeY, sizeX)
    # print(domain)

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
        domain = updateValues(domain, currTime)
        plotSpatial(domain, currTime)
        simTime.append(currTime)
        asymptomatic.append(np.count_nonzero(domain == 0))
        affected.append(np.count_nonzero(domain == 1))
        recovery.append(np.count_nonzero(domain == 2))
    temporal_dynamics = [simTime, asymptomatic, affected, recovery]
    plotDynamics(temporal_dynamics)

main()
