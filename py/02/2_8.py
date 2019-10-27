def odd_or_even(n):
    if n % 2 == 0:
        print ('{}는 짝수이다.'.format(n))
        k = 'even'
    elif n %2 != 0:
        print ('{}는 홀수이다.'.format(n))
        k = 'odd'
    return n
print (odd_or_even(9))
print (odd_or_even(4))
