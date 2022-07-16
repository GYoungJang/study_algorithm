from typing import Any, Sequence
'''Any는 제약이 없는 임의의 자료형
Sequence는 시퀀스형을 의미'''


def max_of(a: Sequence) -> Any:
    ''' 매개변수 a의 자료형은 Sequence
    반환하는 것은 임의의 자료형인 Any
    시퀀스형 a 원소의 최댓값을 반환'''
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


print('-' * 20)
print(__name__)
if __name__ == '__main__':
    '''__name__은 모듈 이름을 나타내는 변수
    max.py이 메인 프로그램으로직접 실행되면 __name__ == '__main__'
    하지만 다른 곳에 모듈로 import 되면 __name__ == '해당파일의 이름', 즉 'max'.
    17행의 if문은 max.py를 직접 실행한 경우에만 참이 되어 실행이 됨.
    '''

    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.'))

    print(f'최댓값은 {max_of(x)}입니다.')
