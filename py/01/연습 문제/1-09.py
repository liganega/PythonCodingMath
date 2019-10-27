def rotation(list_a):
    new_list = []
    new_list.append(list_a[-1])
    new_list = new_list + (list_a[:-1])
    return new_list

def n_rot(list_a, n):
    for i in range(n):
        list_a = rotation(list_a)
    return list_a
a = [1,2,3,4,5,6,7,8,9]
print (n_rot(a,3))