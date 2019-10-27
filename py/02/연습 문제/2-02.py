import numpy as np

def random95():
    a = 0
    number = []
    while a < 95:
        a = np.random.randint(1, 101)
        number.append(a)
    return number

print (random95())