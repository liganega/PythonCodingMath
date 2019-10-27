x = np.arange(-7, 5, 0.1)
y = np.arange(-1, 8, 0.1)

count = 0
for i in x:
    for j in y:
        if (i + 5 >= j) and (-2*i+7 >= j) and (j >= 0):
            count += 1
print ('소수 1째짜리 쌍의 갯수는 {}이다.'.format(count))

print (2352 * 0.01)