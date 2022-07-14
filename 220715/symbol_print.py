print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?'))

for i in range(n):
    if i % 2:
        print('-', end='')
    else:
        print('+', end='')

print()

'''위의 코드는 문제점이 있음 1. for문 반복마다 if문 수행 2. 상황에 따라 유연하게 수정하기 어려움. 
예를 들어 i가 1부터 시작하게 하면 for문 안의 print함수의 호출 순서를 바꿔줘야 함'''

# --------위의 코드보다 효율적인 코드--------
print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?'))

for i in range(n//2):
    print('+-', end='')  # +-를 n//2개 출력

if n % 2:
    print('+', end='')  # n이 홀수일 때만 + 출력

print()

# *를 n개 출력하되 w개마다 줄바꿈 하기1

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?'))
w = int(input('몇 개마다 줄바꿈 할까요?'))

for i in range(n):  # n번 반복
    print('*', end='')
    if i % w == w - 1:  # n번 판단
        print()  # 줄바꿈

if n % w:  # 1번 판단
    print()  # 줄바꿈

'''위의 코드는 for문을 반복할 때마다 if문을 실행하므로 효율적이지 않음'''

# ------위의 코드보다 효율적인 코드----------

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?'))
w = int(input('몇 개마다 줄바꿈 할까요?'))

for i in range(n//w):  # n // w번 반복
    print('*' * w)

rest = n & w
if rest:  # 1번 판단
    print('*' * rest)
