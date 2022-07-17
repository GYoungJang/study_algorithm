# 자료형을 정하지 않은 리스트 원소 확인하기

import copy            # deepcopy를 사용하기 위한 copy 모듈을 임포트
arr_ = [15, 64, 7, 3.14, [32, 55], 'ABC']

for i in range(len(arr_)):
    print(f'arr_[{i}] = {arr_[i]}')

# --------------------------
# 리스트 얕은, 깊은 복사

arr1 = [[1, 2, 3], [4, 5, 6]]
arr2 = arr1.copy()       # arr1을 arr2로 얕은 복사
arr1[0][1] = 9
print(arr1)
print(arr2)


arr3 = [[1, 2, 3], [4, 5, 6]]
arr4 = copy.deepcopy(arr3)       # arr3을 arr4로 깊은 복사

arr3[0][1] = 7
print(arr3)                      # 9 출력
print(arr4)                      # 영향 없음
