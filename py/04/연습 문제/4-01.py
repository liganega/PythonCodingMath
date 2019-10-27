def custom_zip(a,b):
    if len(a) != len(b):
        print('두 입력값의 길이가 다릅니다.')
    else:
        n = len(a)
        c = []
        for i in range(n):
            c.append((a[i],b[i]))
        return c
    
a = [1,2,3]
b = ['a','b','c']
print (custom_zip(a,b))