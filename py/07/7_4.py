def ReLU(y):
    if y > 0:
        return y
    else:
        return 0

def error(y, t):
    return t - y
                                
n = 400
W = np.array([0, 0, 0])
learning_rate = 0.05

for i in range(n):
    t = 0
    X = np.random.randint(2, size = 3)
    if X[1] == 1:
        t = 1
    y = ReLU(input_total(X, W))
    e = error(y, t)
    learning = learning_rate * e
    W = W + learning * X
    
    for j in range(len(W)):
        if W[j] > 1:
            W[j] = 1
    
    if i % 50 == 0:
        print ('{}번째 학습이며 이때 가중치 W는 {}'.format(i, W))