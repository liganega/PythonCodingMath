learning_rate = 0.01
learning = learning_rate*e_R
print (learning)

W = W + learning * X_R
print (W)
print ('')

t_G = 1
X_G = np.array([0,1,0])
Y_G = activation_func(input_total(X_G,W))
e_G = error(Y_G, t_G)
print('expectation : {}'.format(Y_G))
print('error : {}'.format(e_G))

learning = learning_rate * e_G
W = W + learning * X_G
print (W)
print ('')

t_B = 0
X_B = np.array([0,0,1])
Y_B = activation_func(input_total(X_B,W))
e_B = error(Y_B, t_B)
print('expectation : {}'.format(Y_B))
print('error : {}'.format(e_B))

learning = learning_rate * e_B
W = W + learning * X_B
print (W)
