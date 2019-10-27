import numpy as np
import matplotlib.pyplot as plt

XR = 0
XG = 0
XB = 0

WR = 0
WG = 0
WB = 0

X = np.array([XR, XG, XB])
W = np.array([WR, WG, WB])

def input_total(X,W):
    y = np.multiply(X,W)
    return np.sum(y)

y = input_total(X,W)
print (y)

xx = np.arange(-10,11)
yy = np.zeros(len(xx))
for i in range(len(xx)):
    if xx[i] >= 1:
        yy[i] = 1
plt.plot(xx,yy)
plt.grid()

def activation_func(y):
    if y >= 1:
        return 1
    else:
        return 0
print (activation_func(y))

t = 0
def error(y, t):
    return t - y
e = error(y, t)
print('expectation : {}'.format(y))
print('error : {}'.format(e))

expectation : 0
                                