def pibonacci(n):
    pib = [1,2]
    for i in range(2,n):
        pib.append(pib[-1]+pib[-2])
    return pib[-1]

print (pibonacci(5))