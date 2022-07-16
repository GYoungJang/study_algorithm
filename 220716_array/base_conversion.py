# 10진수 정수를 입력받아 2~36진수로 변환하여 출력하기
def base_conv(x: int, r: int) -> str:
    '''정수 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환'''
    d = ''  # 변환 후의 문자열
    dstr = '0123456789ABCDEFGHIJKLMNOPQRSTUVXYZ'

    while x > 0:
        d += dstr[x % r]
        x //= r

    return d[::-1]


if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:
        while True:  # 음이 아닌 변환할 정수를 입력받음
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요 : '))
            if no > 0:
                break

        while True:  # 2 ~ 36진수의 정수값을 입력받음
            # conversion decimal인가?
            cd = int(input('2부터 36까지의 어떤 진수로 변화할까요? : '))
            if 2 <= cd <= 36:
                break

        print(f'{cd}진수로는 {base_conv(no, cd)}입니다.')

        retry = input('한번 더 변환할까요? (Y ··· 예 / N ··· 아니요): ')
        # if retry in {'N', 'n'}:
        if retry == 'N' or 'n':
            print('변환을 종료합니다.')
            break

# n진수를 10진수로 변환하기
# def base_conv1(n, base):
#   decimal = 0
#   for idx, val in enumerate(str(n)[::-1]):
#     decimal += (base ** idx) * int(val)
#   return decimal

# print(base_conv1(21, 3))
