import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x,y)

plt.figure()
plt.plot(x,y, linewidth = 4)

plt.figure()
plt.plot(x,y, c = 'r', linewidth = 4)

plt.figure()
plt.plot(x,y, c = 'r', linewidth = 4, alpha = 0.5)

plt.figure()
plt.scatter(x,y, c = 'g', s = 100)
plt.plot(x,y, c = 'g', alpha = 0.5)

plt.figure()
plt.scatter(x,y, c = 'g', s = 100)
plt.plot(x,y, c = 'g', alpha = 0.5)
plt.grid()

plt.figure(figsize = (6,6)) 
plt.scatter(x,y, c = 'g', s = 100)
plt.plot(x,y, c = 'g', alpha = 0.5)
plt.grid()

plt.figure(figsize = (6,6)) 
plt.scatter(x,y, c = 'g', s = 100)
plt.plot(x,y, c = 'g', alpha = 0.5)
plt.grid()
plt.xlim([0,6])
plt.ylim([0,12])

plt.figure(figsize = (6,6)) 
plt.scatter(x,y, c = 'g', s = 100, label = 'dot graph')
plt.plot(x,y, c = 'g', alpha = 0.5, label = 'line graph')
plt.grid()
plt.legend()

plt.figure(figsize = (6,6)) 
plt.scatter(x,y, c = 'g', s = 100, label = 'dot graph')
plt.plot(x,y, c = 'g', alpha = 0.5, label = 'line graph')
plt.grid()
plt.legend()
plt.xticks(fontsize = 14, color = 'b')
plt.yticks(fontsize = 25, color = 'y')

plt.figure(figsize = (6,6)) 
plt.scatter(x,y, c = 'g', s = 100, label = 'dot graph')
plt.plot(x,y, c = 'g', alpha = 0.5, label = 'line graph')
plt.grid()
plt.xticks(fontsize = 14, color = 'b')
plt.yticks(fontsize = 25, color = 'y')
plt.legend(fontsize = 20,  loc = 4)


plt.figure(figsize = (6,6)) 
plt.scatter(x,y, c = 'g', s = 100, label = 'dot graph')
plt.plot(x,y, c = 'g', alpha = 0.5, label = 'line graph')
plt.grid()
plt.xticks(fontsize = 14, color = 'b')
plt.yticks(fontsize = 25, color = 'y')
plt.legend(fontsize = 20,  loc = 4)
plt.title('y = 2x', fontsize = 30)

plt.figure(figsize = (6,6)) 
plt.scatter(x,y, c = 'g', s = 100, label = 'dot graph')
plt.plot(x,y, c = 'g', alpha = 0.5, label = 'line graph')
plt.grid()
plt.xticks(fontsize = 14, color = 'b')
plt.yticks(fontsize = 25, color = 'y')
plt.legend(fontsize = 20,  loc = 4)
plt.xlabel('Sun light', color = 'c', fontsize = 19)
plt.ylabel('Apple sweet', color = 'm', fontsize = 30)
plt.title('y = 2x', fontsize = 30)