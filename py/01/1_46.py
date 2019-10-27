def union_all(*lists):
    """여러개의 입력값으로부터 합집합 구하기
    list_a, list_b, list_c 로 부터 합집합을 구하려면 2번의 합집합이 필요하다.
    즉 list_a와 list_b의 합집합을 구하고, 그 결과와 list_c의 합집합을 구하면 된다.
    n개의 입력값으로부터 합집합은 n-1번의 합집합이 필요하다.
    """
    
    u = union(lists[0], lists[1])   # 처음은 list[0]과 list[1]의 합집합을 구하여 u라 정의하고 
    for i in lists[2:]:             # for 문에서 list[2]부터 다시 합집합을 구한다. 
        u = union(u, i) 
        u.sort()
    return u

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

a = [1,3,6,5,7]
b = [1,5,2,7,3]
c = [4,2,8,9,5]
print(union_all(a,b,c))
print(intersection_all(a,b,c))
 
