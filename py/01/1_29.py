a = [1,2,3,1]
new_a = []                # 공집합을 만들어 new_a로 지장하고
for i in a:               # a의 원소에대해
    if i not in new_a:    # i가 new_a에 없으면
        new_a.append(i)   # new_a에 i를 추가하여라
print (new_a)