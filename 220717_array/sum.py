# 1부터 n까지 정수의 합 구하기

def sum_1ton(n):
    '''1부터 n까지 정수의 합 구하기'''
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    return sum


num = int(input('숫자를 입력해주세요 : '))
print(f'1부터 {num}까지 정수의 합은 {sum_1ton(num)}입니다.')
'''int가 immutable이기 때문에 실제 인수 num의 값은 변하지 않음
매개변수 n은 업데이트 되는 시점에 다른 객체를 생성하고 그 객체를 참조함.'''
