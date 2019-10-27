import numpy as np

x = np.arange(2, 100)
for i in x:
    if (np.sqrt(i+3)-1) == np.sqrt(i - np.sqrt(i-2)):
        print (i)
