fruit = ['strawberry', 'grape', 'apple', 'mango', 'orange']
a = list(enumerate(fruit))
print (a)

a = [0,1,2,3,4]
for idx, val in enumerate(fruit):  # list a의 원소 0,1,2,3,4를 i라 하고
    print (idx, val)  # 매번 i를 출력시켜라.
    

a = [10,9,8,7,6,5,4,3,2,1,0]
for idx, val in enumerate(a):
    print (idx, val)  # idx는 순서를, val을 값을 나타낸다.