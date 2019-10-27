import pandas as pd

print (df.set_index('Team'))
print ('')
print (df.set_index('Team').loc['Korea Republic'])
print ('')
print (df.set_index('Team').loc['Korea Republic'].mean())
print ('')
print (df.set_index('Team').loc['Korea Republic'].std())