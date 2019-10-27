import numpy as np

def lotto():
    number = []                               # lotto 6개 숫자를 넣을 공집합 number를 만들고
    for i in range(6):                        # 6번의 숫자만들기에서
        new_element = np.random.randint(1,46) # 1에서 45까지의 난수를 new_element로 지정하고
        if new_element not in number:         # new_element가 number의 element에 없으면
            number.append(new_element)        # number에다가 new_element를 추가하여라
    return number

print (lotto())