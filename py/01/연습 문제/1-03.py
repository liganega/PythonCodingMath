def number_intersection(a,b):
    str_a = str(a)
    str_b = str(b)
    c = []
    c = intersection(str_a, str_b)   # 교집합은 미리 만들어 놓았으니 불러오기만 하면 됩니다.
    c.sort()
    return c

a = 38472
b = 173
c = number_intersection(a,b)
print (c)