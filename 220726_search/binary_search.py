# 이진 검색 알고리즘을 사용하려면 배열의 데이터가 정렬되어 있어야 함.
# 이진 검색의 종료조건 1. 중앙값과 찾는 값이 일치하는 경우 2. 검색 범위가 더 이상 없는 경우
# 왜 이진 검색의 시간 복잡도는 log n 일까...

from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    '''시퀀스 a에서 key와 일치하는 원소를 이진 검색'''
    front = 0                          # 검색 범위 맨 앞 원소의 인덱스
    rear = len(a) - 1                  # 검색 범위 맨 끝 원소의 인덱스

    while True:
        center = (front + rear) // 2      # 중앙 원소의 인덱스
        if a[center] == key:
            return center                 # 검색 성공
        elif a[center] < key:
            front = center + 1            # 검색 범위를 뒤쪽 절반으로 좁힘
        else:
            rear = center - 1             # 검색 범위를 앞쪽 절반으로 좁힘

        if front > rear:
            break
    return -1            # 검색 실패


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num           # 원소 수가 num인 배열 생성
    print('배열 데이터를 오름차순으로 입력하세요.')

    x[0] = int(input('x[0] : '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= x[i - 1]:              # 바로 직전에 입력한 원소값보다 큰 값을 입력
                break

    key = int(input('검색할 값을 입력하세요 : '))        # 검색할 키값을 입력

    idx = bin_search(x, key)                            # 키값과 같은 원소를 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다. ')
