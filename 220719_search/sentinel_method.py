# 선형 검색 알고리즘을 보초법으로 수정

from typing import Any, Sequence
import copy


def seq_search(seq: Sequence, key: Any) -> int:
    '''시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)'''
    a = copy.deepcopy(seq)  # seq를 복사
    a.append(key)           # 보초 key를 추가

    i = 0
    while True:
        if a[i] == key:
            break          # 검색에 성공하면 while 문을 종료
        i += 1
    return -1 if i == len(seq) else i


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요 : '))        # num 값을 입력
    x = [None] * num                                # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    key = int(input('검색할 값을 입력하세요 : '))        # 검색할 key를 입력받기

    idx = seq_search(x, key)                            # key 값과 같은 원소를 x에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{i}에 있습니다.]')
