n = 400
W = np.array([0, 0, 0])
learning_rate = 0.05

WR_save = []
WG_save = []
WB_save = []
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
    WR_save.append(W[0])
    WG_save.append(W[1])
    WB_save.append(W[2])
    if i % 50 == 0:
        print ('{}번째 학습이며 이때 가중치 W는 {}'.format(i, W))

plt.plot(range(n), WR_save, 'r', label = 'Red learning')
plt.plot(range(n), WG_save, 'g', label = 'Green learning')
plt.plot(range(n), WB_save, 'b', label = 'Blue learning')
plt.legend(fontsize = 15)
plt.grid()
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.xlabel('number of learning', fontsize = 15)
plt.ylabel('Accuracy', fontsize = 15)