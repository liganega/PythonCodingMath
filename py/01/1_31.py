a = [1,2,3]
b = [3,4,5]

c = []                     # 합집합을 웅선 공집합으로 만들어 놓고
for i in a:                # a에 속한 모든 요소 i에 대해서 순서대로 실행시키자. 
    if i not in b:         # 만약 i가 b에 속하지 않는다면
        c.append(i)        # 합집합 c에 i를 추가하여라.
c = c + b
c.sort()
print (c)
