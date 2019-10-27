"""함수의 정의"""
def sum_all(*args):
    total_sum = 0                    # total_sum을 우선 0으로 만들고
    for i in args: 
        # 여러가지 입력값 args의 각 원소 i에 대해
        total_sum = total_sum + i    # total_sum에다 i를 더하라
    return total_sum

print (sum_all(3,6,9))
print (sum_all(3,1,5,6,4,7))