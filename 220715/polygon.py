# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기
# 약수 나열

area = int(input('직사각형의 넓이를 입력하세요 : '))

for i in range(1, area+1):  # 1부터 사각형의 넓이 계산
    if i * i > area:  # 사각형의 넓이 초과
        break
    if area % i:  # i로 나누어 떨어지면 for문의 다음 반복으로 넘어감
        continue
    print(f'{i} x {area//i}')

# --------------------------------------------------
# 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

print('왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기')
n = int(input('짧은 변의 길이를 입력하세요 : '))

for i in range(n):  # 행
    for j in range(i+1):  # 열
        print('*', end='')
    print()

# -----------------------------------------------------
# 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

print('오른쪽 아래가 직각인 이등변 삼각형으로 * 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요 : '))

for i in range(1, n+1):
    for _ in range(n - i):  # 공백 출력
        print(' ', end='')
    for _ in range(i):  # * 출력
        print('*', end='')
    print()
