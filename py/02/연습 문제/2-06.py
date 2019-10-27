a = [1,2,3,4]
number = ''
for i in range(len(a)):
    number = number + str(a[i])
number = int(number)
print (number)

a = [1,2,3,4]
def list_to_number(a):
    number = ''
    for i in range(len(a)):
        number = number + str(a[i])
    number = int(number)
    return number

print (list_to_number([3,2,4,6,7,4,2,69]))
print (str(a[0]))
number = ''
print (number + str(3))