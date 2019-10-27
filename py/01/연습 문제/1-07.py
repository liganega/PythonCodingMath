def subset_or_not(a,b):
    a.sort()
    if intersection(a,b) == a:
        print ('a는 b의 부분집합')
    else:
        print ('a는 b의 부분집합이 아니다.')
        
a = [1,3,5,7]
b = [1,3,5,7,9]
print (subset_or_not(a,b))

b.remove(3)
print (subset_or_not(a,b))