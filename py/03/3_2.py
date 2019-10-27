even = lambda x : x % 2 == 0
print (list(filter(even, range(1,11))))

print (list(filter(lambda x: x % 2 == 0, [3, 1, 4, 2, 9])))

a = [3,1,4,2,9]

def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

even_numbers = []
for i in a:
    if even(i):
        even_numbers.append(i)
print(even_numbers)