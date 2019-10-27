def rotation(list_a):
    new_list = []
    new_list.append(list_a[-1])
    new_list = new_list + (list_a[:-1])
    return new_list

a = [1,2,3,4,5,6,7,8,9]
print (rotation(a))