# 배열 원소의 최댓값을 구해서 출력하기(원소값을 난수로 생성)

import random
from max import max_of

print('난수의 최댓값을 구합니다.')
num = int(input('난수의 개수를 입력하세요 : '))
low = int(input('난수의 최솟값을 입력하세요 : '))
high = int(input('난수의 최댓값을 입력하세요 : '))
x = [None] * num      # 원소 수가 num인 리스트 생성

for i in range(num):
    x[i] = random.randint(low, high)  # low 이상 high 이하인 정수 난수

print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.')
