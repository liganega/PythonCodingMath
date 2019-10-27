import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print (s)
print ('')
print (s+s)
print ('')

print (s*2)
print ('')

print (s**2)
print ('')
