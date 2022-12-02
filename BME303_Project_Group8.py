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

# adds initial covid (3) individuals in the simulation
# they are added randomly amongst a 30 day iteration
# this is to ensure as the simulation runs, we will always get a positive covid individual
# this function is to account for the outside introduction of the virus to our sample community.

def addCovid(matrix): # creating a matrix
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

# this function creates another matrix that goes through the 30 day immunity and assess a contact in the location of the grid
# from the location of the contact we use a series of if and else statements to move and assign the remaining (0,1,2)
# the contact rate is the rate of contact from the first covid individual.
# r is a random float number from 0-1.0, this is in percentage.
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

#this function will generate empty states randomly to the spaces in the matrix grid from the individuals who have covid.
# This clears up any possible backlog for the recovery and no symptomp state throughout the 100th iterations
# this takes account of how in real life covid death rates were recorded
def covidDeaths(matrix):
    for idx, value in np.ndenumerate(matrix):
        if value == 3:
            r = random.random()
            if r < .1:
                matrix[idx] = 0
        else:
            continue
    return matrix
# this function will assign the asymptomatic state to the covid indivduals.
# asymptomatic state is only assigned to covid indivduals.
# this state is not an empty state, the population of this state is recorded that is why we need to take an account of this state
def asymptomaticRule(matrix):
    count = 0
    while count != 10:
        x = random.randint(0, 29)
        y = random.randint(0, 29)

        if matrix[x, y] == 3:
            matrix[x, y] = 1
            count+=1
    return matrix
# this function abides the 30 day immunity period.
# every for loop iterates to this function.
# count will never exceed 300
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
    #calling of time counter
    random.seed(time.time())
    #assign states as empty lists
    simTime, nosymptoms, asymptomatic, contact, covid = [], [], [], [], []
    #start of time count in days
    currTime = 0
    #create the matrix of 900 empty spaces
    matrix = np.zeros(900).reshape(30,30)
    #call add covid function this is the starting 10 indivduals with covid
    matrix = addCovid(matrix)
    # update matrix and then plot the starting location of the covid individuals
    plotSpatial(matrix,currTime)

    #During the two weeks (14 days) of quaratine the covid indiviuals will also create the spread in the matrix
    for currTime in range(1, 14):
        #update matrix after calling addContact this is the start of the moore nieghborhood
        matrix = addContact(matrix)
        plotSpatial(matrix, currTime) # plot the add contact function and see how neighboring spaces are effected
        matrix = covidDeaths(matrix) # update matrix to include any possible deaths within the quarentine
        simTime.append(currTime) # fill the empty simulation list with the current time starting at day 1.

        # creating empty numpy arrays and assigning them on how they will be recorded and later turned into plot lines
        nosymptoms.append(np.count_nonzero(matrix == 0))
        asymptomatic.append(np.count_nonzero(matrix == 1))
        contact.append(np.count_nonzero(matrix == 2))
        covid.append(np.count_nonzero(matrix == 3))
    #this is main for loop function for the remaining 14-100 days. We want to call all the functions and keep track of the time for plotting
    for currTime in range(14,101):
        matrix = addContact(matrix)
        matrix = covidDeaths(matrix)
        simTime.append(currTime)
        matrix = asymptomaticRule(matrix)
        plotSpatial(matrix, currTime)
        #to adept to the immunity period, no function chainging state will be called on this day
        if currTime%30 == 0:
            matrix = immunityPeriod(matrix)
        nosymptoms.append(np.count_nonzero(matrix == 0))
        asymptomatic.append(np.count_nonzero(matrix == 1))
        contact.append(np.count_nonzero(matrix == 2))
        covid.append(np.count_nonzero(matrix == 3))
    #graphing of the temporal dynamics with the numpy arrays as parameters
    temporal_dynamics = [simTime, nosymptoms, asymptomatic, contact, covid]
    #calling of plot dynamics to print the temporal line
    plotDynamics(temporal_dynamics)
    #creates gif of .2 long this is the visual of the matrix and shows how the states spread
    imageio.mimwrite('matrixgif.gif',imgList, duration = .2)
#calling of main function so that it will run and output our desired graphs.
main()
