import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

def saving(money, years, rate):
    result = money*(1+rate/100)**years
    return result

money = 10000
years = np.arange(0,11)
rate = [3, 5, 7]
total_money = np.zeros((len(rate), len(years)))
for i in range(len(rate)):
    for j in range(len(years)):
        total_money[i,j] = saving(money, years[j], rate[i])
    plt.plot(years, total_money[i,:], label = '{}%'.format(rate[i]))
plt.legend(fontsize = 14)
plt.grid()
plt.xlabel('Years', fontsize = 14)
plt.ylabel('Total money', fontsize = 14)

money = 10000
years = np.arange(0,25)
rate = [3, 5, 7]
total_money = np.zeros((len(rate), len(years)))
plt.figure()
for i in range(len(rate)):
    for j in range(len(years)):
        total_money[i,j] = saving(money, years[j], rate[i])
    plt.plot(years, total_money[i,:], label = '{}%'.format(rate[i]))
plt.axhline(y = 20000, color = 'red', label = '20000')
plt.legend(fontsize = 14)
plt.grid()
plt.xlabel('Years', fontsize = 14)
plt.ylabel('Total money', fontsize = 14)


for i, val in enumerate(total_money[0,:]):
    if val > 20000:
        print ('{}% rate takes {} years'.format(3, i))
        break
    
for i, val in enumerate(total_money[1,:]):
    if val > 20000:
        print ('{}% rate takes {} years'.format(5, i))
        break
    
for i, val in enumerate(total_money[2,:]):
    if val > 20000:
        print ('{}% rate takes {} years'.format(7, i))
        break