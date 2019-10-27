import numpy as np
import matplotlib.pyplot as plt

print (np.roots([121, -1105.5, 1100]))

AA = np.arange(11, 100, 11)
print (AA)
for i in AA:
    if len(str(i**2)) == 4:
        if (int(str(i**2)[:2])/11) == (i/11 - 1):
            if (int(str(i**2)[2:])/11) == (i/11/2):
                print (i)