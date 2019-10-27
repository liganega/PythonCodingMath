def union(a,b):
    c = []
    for i in a:                # a에 속한 모든 요소 i에 대해서 순서대로 실행시키자. 
        if i not in b:         # 만약 i가 b에 속하지 않는다면
            c.append(i)        # 합집합 c에 i를 추가하여라.
    c = c + b                  # b에 속하지 않는 a와 b가 더해집니다. 
    c.sort()                 
    return c

def intersection(a,b):
    c = []               
    for i in a:
        if i  in b:
            c.append(i)
    c.sort()
    return c

def complement(a,b):
    c = a + []
    for i in b:   
        if i in a: 
            c.remove(i) 
    c.sort()
    return c

def double_complement(a,b):
    c = union(a,b) 
    d = intersection(a,b)
    e = complement(c,d)
    e.sort()
    return e


a = [1,3,5,7,9,2]
b = [2,4,6,8,0,7]

double_complement(a,b)