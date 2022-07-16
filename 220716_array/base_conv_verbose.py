def base_conv_verbose(x: int, r: int) -> str:
    d = ''
    dstr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))  # 변환하기 전의 자릿수

    print(f'{r:2} | {x:{n}}')
    while x > 0:
        print('  +' + (n + 2) * '-')
        if x // r:
            print(f'{r:2} | {x // r:{n}} ··· {x % r}')
        else:
            print(f'     {x // r:{n}} ··· {x % r}')
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

        print(f'{cd}진수로는 {base_conv_verbose(no, cd)}입니다.')

        retry = input('한번 더 변환할까요? (Y ··· 예 / N ··· 아니요): ')
        # if retry in {'N', 'n'}:
        if retry == 'N' or 'n':
            print('변환을 종료합니다.')
            break
