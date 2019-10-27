x = np.arange(-7, 5)
y = np.arange(-1, 8)

count = 0
for i in x:
    for j in y:
        if (i + 5 >= j) and (-2*i+7 >= j) and (j >= 0):
            print (i,j)
            count += 1
print ('정수의 갯수는 {}이다.'.format(count))