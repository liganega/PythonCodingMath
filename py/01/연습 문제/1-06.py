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

def intersection_all(*lists):
    """여러개의 입력값으로부터 교집합 구하기
    list_a, list_b, list_c 로 부터 교집합을 구하려면 2번의 교집합이 필요하다."
    n개의 입력값으로부터 교집합은 n-1번의 교집합이 필요하다."
    """
    
    d = intersection(lists[0], lists[1])   # 처음은 list[0]과 list[1]의 교집합을 구하여 c라 정의하고 
    for i in lists[2:]:                    # for 문에서 list[2]부터 다시 교집합을 구한다. 
        d = intersection(d, i) 
        d.sort()
    return d


def xor3(a,b,c):
    d = complement(a,union(b,c)) + complement(b, union(a,c)) + complement(c, union(a,b))
    d = d + intersection_all(a,b,c)
    d.sort()
    return d

a = [1,2,3,4]
b = [5,2,3,6]
c = [7,6,3,4]

xor3(a,b,c)