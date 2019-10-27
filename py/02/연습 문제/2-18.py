def digit_expand(a, n):   # n은 진수를 의미합니다. 10진수면 n에 10을 넣으면 됩니다.
    digit_10 = []
    while a // n != 0: 
        e = a % n  
        digit_10.append(e)
        a //= n 

    digit_10.append(a)
    digit_10.reverse()
    
    return digit_10

def list_to_number(a):
    number = ''
    for i in range(len(a)):
        number = number + str(a[i])
    number = int(number)
    return number


def Number_system_change(number, n, m):
##################################
# number : 변형하려는 숫자
# n : 현재의 진법
# m : 미래의 진법
# number의 각 숫자가 n보다 크거나 같으면 error
##################################
    num_str = str(number)  # 325
    len_num = len(num_str) # 3
    
    # 우선 10진법으로 바꾸기
    number_10 = 0
    for i, num in enumerate(num_str):     # (0,'3'), (1,'2'), (2,'5') 형태의 (i,num)이 됨
        num_int = int(num)                # 문자형'3'을 정수형 3으로 변형
        if num_int >= n:                  # 2진법에 2보다 큰 숫자가 오면 안되므로 이 조건문을 써야함
            print ('{}는 {}보다 크거나 같으니 {}진법의 수가 아니다.'.format(num_int, n, n))
            break                         # 이렇게 잘못하면 break로 if와 for 반복을 끝냄
        else:
            number_10 += num_int*n**(len_num-i-1)  #(3 x 6**2) + (2 x 6) + (5 x 1) 하는 과정임

    # 10진법을 m진법으로 바꾸기
    number_m = digit_expand(number_10, m)  
    return number_m

a = Number_system_change(621, 7, 10)
b = Number_system_change(3213, 4, 10)
a = list_to_number(a)
b = list_to_number(b)
print (a)
print (b)
print ('{}개의 수가 있다.'.format(a-b))