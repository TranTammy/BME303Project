# define r
r = 0.31
# define array x to hold 12 values
x = [0] * 13
# initializes index 0
x[0] = 0.43
# counter n
n = 0

#opens file with new input
outfile = open("BME303_Lab8_P1_TammyTran.txt", "w")
# for loop to 12
for n in range(0,12):
    x[n+1] = x[n] + r * x[n] * (1.0 - x[n])
    # prints values
    outfile.write('At year ' + str(n) + ', the population density is ' + str(x[n]) + '\n')
    # adds 1 to n
    n = n + 1
outfile.write('At year ' + str(n) + ', the population density is ' + str(x[n]) + '\n')
# close file
outfile.close()
