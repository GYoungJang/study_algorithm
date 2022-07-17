# 리스트에서 임의의 원솟값을 업데이트 하기
def change(lst, idx, val):
    '''lst[idx}의 값을 val로 업데이트'''
    lst[idx] = val


arr_ = [11, 22, 33, 44, 55]
print('x = ', arr_)

index = int(input('업데이트할 인덱스를 선택하세요 : '))
value = int(input('새로운 값을 입력하세요 : '))

change(arr_, index, value)
print(f'arr_ = {arr_}')
'''list가 mutable이기 때문에 함수 안에서 업데이트한 값이 원래 호출한 곳으로 전달됨'''
