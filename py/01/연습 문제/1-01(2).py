a = ['apple', 'melon', 'orange'] 
b = ['chicken', 'pig', 'cow']

b[1] = 'melon'

print(b)

c = []
for i in a:                # a에 속한 모든 요소 i에 대해서 순서대로 실행시키자. 
    if i not in b:         # 만약 i가 b에 속하지 않는다면
        c.append(i)        # 합집합 c에 i를 추가하여라.
c = c + b
c.sort()
print (c)