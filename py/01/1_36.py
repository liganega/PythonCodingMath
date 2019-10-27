a = [1,2,3]
b = [3,4,5]
c = a.copy()

for i in b:          # b원소가
    if i in a:       #i가 a에 속한다면
        c.remove(i)  #c에서 i를 지워라
print (c)
print (a)