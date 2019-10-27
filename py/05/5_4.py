import pandas as pd
import numpy as np

d = {'a' : 0., 'b' : 1., 'c' : 2.}
f = pd.Series(d)
print (f)
print ('')

print (f[0])
print (f[:])
print (f['a'])


print ('b'in f)
print ('d'in f)

print (f.get('a'))
print (f.get('d'))