a = ['오이', '상추', '고추']
b = ['사과', '수박']
c = ['닭', '소', '돼지']
d = '오이'

if d in a:
    print ('{}는 야채'.format(d) )
elif d in b:
    print ('{} 는 과일'.format(d))
elif d in c:
    print ('{}는 고기'.format(d))
else:
    print ('{}는 야채도 아니고 과일도 아니고 고기도 아니다.'.format(d))

d = '아이폰'
if d in a:
    print ('{}는 야채'.format(d))
elif d in b:
    print ('{}는 과일'.format(d))
elif d in c:
    print ('{}는 고기' .format(d))
else:
    print ('{}는 야채도 아니고 과일도 아니고 고기도 아니다.' .format(d))