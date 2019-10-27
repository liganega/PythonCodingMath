BMI = lambda weight, height : weight / (height)**2
print (BMI(68,1.75))

def fat_or_not(weight, height):
    bmi = BMI(weight, height)
    print ('당신의 BMI는 {}입니다'.format(bmi))
    if bmi > 35:
        print ('당신은 고도비만입니다.')
    elif 30 <= bmi < 35:
        print ('당신은 중등도비만입니다.')
    elif 25 <= bmi < 30:
        print ('당신은 경도비만입니다.')
    elif 23 <= bmi < 25:
        print ('당신은 과체중입니다.')
    elif 18.5 <= bmi < 22.9:
        print ('당신은 정상입니다.')
    elif bmi < 18.5:
        print ('당신은 저체중입니다.')
        
fat_or_not(68,1.75)