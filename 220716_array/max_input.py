from max import max_of
'''모듈 max를 import 했지만 max.py 파일 내에서 13행의 if문은 실행이 안됨
왜냐하면 다른 프로그램에서 import 되었기 때문에 __name__ == '__main__' 아니기 때문'''

print('배열의 최댓값을 구합니다.')
print('주의: "END"를 입력하면 종료합니다.')

number = 0
x = []  # 빈 리스트

while True:
    s = input(f'x[{number}]값을 입력하세요 : ')
    if s == 'END':
        break
    x.append(int(s))  # 배열의 맨 끝에 추가
    number += 1

print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')
