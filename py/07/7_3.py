light = np.random.randint(3)
light
                        
n = 1000
W = np.array([0, 0, 0])
learning_rate = 0.01
for i in range(n):
    light = np.random.randint(3)
    if light == 0:
        X = np.array([1, 0, 0])
        t = 0
    elif light == 1:
        X = np.array([0, 1, 0])
        t = 1
    elif light == 2:
        X = np.array([0, 0, 1])
        t = 0
    y = activation_func(input_total(X, W))
    e = error(y, t)
    learning = learning_rate * e
    W = W + learning * X
    
    if i % 50 == 0:
        print ('{}번째 학습이며 이때 가중치 W는 {}'.format(i, W))

light = np.random.randint(2, size = 3)
X = light.copy()

X = np.random.randint(2, size = 3)
if X[1] == 1:
    t = 1
y = activation_func(input_total(X, W))
e = error(y, t)
learning = learning_rate * e
W = W + learning * X

print (W)

n = 200
W = np.array([0, 0, 0])
learning_rate = 0.05

for i in range(n):
    t = 0
    X = np.random.randint(2, size = 3)
    if X[1] == 1:
        t = 1
    y = activation_func(input_total(X, W))
    e = error(y, t)
    learning = learning_rate * e
    W = W + learning * X
    
    if i % 10 == 0:
        print ('{}번째 학습이며 이때 가중치 W는 {}'.format(i, W))