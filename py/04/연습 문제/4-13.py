import numpy as np
import matplotlib.pyplot as plt

def ReLu(*inputs):
    result = np.sum(inputs)
    if result < 0:
        result = 0
    return result

print (ReLu(3,4,5,6,7))
print (ReLu(-9,3,5,4,-6))