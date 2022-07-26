from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    '''시퀀스 a에서 key와 일치하는 원소를 이진 검색 (실행과정을 출력'''
    front = 0              # 검색 범위 맨 앞 원소의 인덱스
    rear = len(a) - 1      # 검색 범위 맨 끝 원소의 인덱스

    print('  |', end='')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4 * len(a) + 2) * '-')

    while True:
        center = (front + rear) // 2            # 중앙 원소의 인덱스
        print('  |', end='')

        if front != center:            # 맨 앞 원소 위에 <- 출력
            print((front * 4 + 1) * ' ' + '<-' +
                  ((center - front) * 4) * ' ' + '+', end='')
        else:
            print((center * 4 + 1) * ' ' + '<+', end='')

        if center != rear:             # 맨 위 원소 위에 -> 출력
            print(((rear - center) * 4 - 2) * ' ' + '->')
        else:
            print('->')

        print(f'{center:3}|', end='')
        for i in range(len(a)):
            print(f'{a[i]:4}', end='')
        print('\n  |')

        if a[center] == key:
            return center    # 검색 성공
        elif a[center] < key:
            front = center + 1  # 검색 범위를 뒤쪽의 절반으로 좁힘
        else:
            rear = center - 1  # 검색 범위를 앞쪽의 절반으로 좁힘
        if front > rear:
            break
    return -1            # 검색 실패


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    print('배열 데이터를 오름차순으로 입력하세요.')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:
                break

    key = int(input('검색할 값을 입력하세요.: '))  # 검색할 ky를 입력

    idx = bin_search(x, key)                     # ky와 같은 값의 원소를 x에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
