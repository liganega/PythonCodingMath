u = [0,1,2,3,4,5,6,7,8,9,0]
a = [1,3,5,7,9]
rest = u + []            # 여집합 rest를 전체집합 u와 똑같이 만들고, 
for i in a:              # a에 속한 모든 요소 i에 대해서 순서대로 실행시키자. 
    if i in u:           # i가 u에 속한다면 
        rest.remove(i)   # rest에서 i를 지워라
print (rest)
