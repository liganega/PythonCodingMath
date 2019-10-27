import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

def Audience(n):
    if n < 10:
        score = 0
    else:
        score = (n-10)*0.5
    return score

def Star(star):
    if star <= 3:
        score = -1
    elif star <= 6:
        score = 0
    elif star <= 9:
        score = 1
    else:
        score = 2
    return score

audience = np.arange(0, 30, 1)
star = np.arange(0,10,1)

score_aud = np.zeros(len(audience))
score_star = np.zeros(len(star))

for i in range(len(audience)):
    score_aud[i] = Audience(audience[i])
    
for j in range(len(star)):
    score_star[j] = Star(star[j])

plt.plot(audience, score_aud)
plt.figure()
plt.plot(star, score_star)

score = np.zeros((len(audience), len(star)))
for i in range(len(audience)):
    for j in range(len(star)):
        score[i,j] = Audience(audience[i]) + Star(star[j])
print (score.shape)
print ('가능한 최고 점수는 {} 이다.'.format(np.max(score)))