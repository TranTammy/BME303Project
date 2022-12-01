import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import random
import time
import imageio
"""
the matrix will have 10 individuals with covid enter the matrix in random areas
rule 1: for a moore neighborhood around a person with covid, every person becomes contact, except 10% become covid
rule 2: for every person with covid, there is a 10% chance they die in which they are replaced with a person that has not met covid
rule 3: every 14 days 20% of those with covid become asymptomatic
rule 4: immunity period every 30 days
"""

# adds initial covid individuals
def addCovid(matrix):
    for i in range(10):
        x = random.randint(0,29)
        y = random.randint(0,29)

        if matrix[x,y] == 0:
            matrix[x,y] = 3
        elif matrix[x,y] != 0:
            while matrix[x,y] != 0:
                x = random.randint(0, 29)
                y = random.randint(0, 29)

                if matrix[x,y] == 0:
                    matrix[x,y] = 3
                    break
    return matrix


def addContact(matrix):
    for (y,x), value in np.ndenumerate(matrix):
        if value == 3:
            if x < 29:
                r = random.random()
                if r < .1:
                    matrix[y, x + 1] = 3 # person gets covid
                elif r > .1:
                    if matrix[y, x + 1] != 3: # if not already covid
                        matrix[y, x + 1] = 2 # person becomes a contact
            if y < 29 and x < 29:
                r = random.random()
                if r < .1:
                    matrix[y + 1, x + 1] = 3
                elif r > .1:
                    if matrix[y+1,x+1] != 3:
                        matrix[y+1,x+1] = 2
            if y < 29:
                r = random.random()
                if r < .1:
                    matrix[y + 1, x] = 3
                elif r > .1:
                    if matrix[y + 1, x] != 3:
                        matrix[y + 1, x] = 2
            if x > 0:
                r = random.random()
                if r < .1:
                    matrix[y,x-1] = 3
                elif r > .1:
                    if matrix[y,x-1] != 3:
                        matrix[y,x-1] = 2
            if y > 0:
                r = random.random()
                if r < .1:
                    matrix[y-1,x] = 3
                elif r > .1:
                    if matrix[y-1,x] != 3:
                        matrix[y-1,x] = 2
            if y > 0 and x > 0:
                r = random.random()
                if r < .1:
                    matrix[y-1,x-1] = 3
                elif r > .1:
                    if matrix[y-1,x-1] != 3:
                        matrix[y-1,x-1] = 2
            if y < 29 and x > 0:
                r = random.random()
                if r < .1:
                    matrix[y+1,x-1] = 3
                elif r > .1:
                    if matrix[y+1,x-1] != 3:
                        matrix[y+1,x-1] = 2
            if y > 0 and x < 29:
                r = random.random()
                if r < .1:
                    matrix[y-1,x+1] = 3
                elif r > .1:
                    if matrix[y-1,x+1] != 3:
                        matrix[y-1,x+1] = 2
        elif value != 3:
            continue
    return matrix

def covidDeaths(matrix):
    for idx, value in np.ndenumerate(matrix):
        if value == 3:
            r = random.random()
            if r < .1:
                matrix[idx] = 0
        else:
            continue
    return matrix

def asymptomaticRule(matrix):
    count = 0
    while count != 10:
        x = random.randint(0, 29)
        y = random.randint(0, 29)

        if matrix[x, y] == 3:
            matrix[x, y] = 1
            count+=1
    return matrix

def immunityPeriod(matrix):
    count = 0
    while count != 300:
        x = random.randint(0, 29)
        y = random.randint(0, 29)

        if matrix[x, y] == 3:
            matrix[x, y] = 1
            count += 1
    return matrix


# plots grid graph
imgList = []
def plotSpatial(matrix, t):
    name = "Covid_Spread_On_Day" + str(t) + ".jpg" #string for each figure at day t
    cmap = colors.ListedColormap(['lightblue','yellow','orange','red'])
    plt.figure(figsize=(7,6)) #generates 7x6 plot
    plt.pcolor(matrix, cmap = cmap, edgecolors='k', linewidths=0.5, vmin=0, vmax=3)

    cbar = plt.colorbar(label="", orientation="vertical", ticks=[0.4,1.1,1.9,2.6])
    cbar.ax.set_yticklabels(['No symptoms', 'Asymptomatic', 'Contact', 'Covid'])
    plt.savefig(name, bbox_inches='tight', pad_inches=0.02)
    imgList.append(imageio.v2.imread(name))
    plt.close()

# plots line graph
def plotDynamics(data):
    fig, axes = plt.subplots(figsize=(10, 10))
    axes.plot(data[0], data[1], label='No Symptoms', color='lightblue')
    axes.plot(data[0], data[2], label='Asymptomatic', color='yellow')
    axes.plot(data[0], data[3], label='Contact', color='orange')
    axes.plot(data[0], data[4], label='Covid', color='red')
    axes.set_xlabel('Time (days)')
    axes.set_ylabel('Number of individuals')
    axes.legend(bbox_to_anchor=(.3, 1), fontsize=13, fancybox=False, shadow=False, frameon=False)
    plt.show()
    plt.savefig('temporalDynamics.pdf', bbox_inches='tight', pad_inches=0.02)
    plt.close()


def main():
    random.seed(time.time())
    simTime, nosymptoms, asymptomatic, contact, covid = [], [], [], [], []

    currTime = 0
    matrix = np.zeros(900).reshape(30,30)
    matrix = addCovid(matrix)
    plotSpatial(matrix,currTime)

    for currTime in range(1, 14):
        matrix = addContact(matrix)
        plotSpatial(matrix, currTime)
        matrix = covidDeaths(matrix)
        simTime.append(currTime)
        nosymptoms.append(np.count_nonzero(matrix == 0))
        asymptomatic.append(np.count_nonzero(matrix == 1))
        contact.append(np.count_nonzero(matrix == 2))
        covid.append(np.count_nonzero(matrix == 3))
    for currTime in range(14,101):
        matrix = addContact(matrix)
        matrix = covidDeaths(matrix)
        simTime.append(currTime)
        matrix = asymptomaticRule(matrix)
        plotSpatial(matrix, currTime)
        if currTime%30 == 0:
            matrix = immunityPeriod(matrix)
        nosymptoms.append(np.count_nonzero(matrix == 0))
        asymptomatic.append(np.count_nonzero(matrix == 1))
        contact.append(np.count_nonzero(matrix == 2))
        covid.append(np.count_nonzero(matrix == 3))
    temporal_dynamics = [simTime, nosymptoms, asymptomatic, contact, covid]
    plotDynamics(temporal_dynamics)
    imageio.mimwrite('matrixgif.gif',imgList, duration = .2)

main()

