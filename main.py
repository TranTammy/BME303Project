import numpy as np
from matplotlib import pyplot as plt

# affected states
a=np.random.rand(500).reshape((20,25))
#recovery state
r=np.random.rand(500).reshape((20,25))
# empty state
e=np.random.rand(500).reshape((20,25))

def spread_function(a,e,r):
    ## put 1a-1c if statments here
    return a*2+r

dc = spread_function(a,e,r)

plt.imshow(dc)
plt.show()