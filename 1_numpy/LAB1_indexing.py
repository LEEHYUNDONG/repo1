import numpy as np

# arr = np.arange(16).reshape(4, 2, 2)
# print(arr)

arr = np.arange(36).reshape(2, 3, 2, 3)
# print(arr)

# print(arr[:, :, :, 0])
# print(arr[..., 0]) # ...으로 여러개의 콜론을 대체할 수 있음

print(arr[0, :, :, 0]) # 두장의 이미지중 첫번째 이미지의 빨간색 정보
print(arr[0, ..., 0])

# [[[[ 0  1  2] 
#    [ 3  4  5]]

#   [[ 6  7  8]
#    [ 9 10 11]]

#   [[12 13 14]
#    [15 16 17]]]


#  [[[18 19 20]
#    [21 22 23]]

#   [[24 25 26]
#    [27 28 29]]

#   [[30 31 32]
#    [33 34 35]]]]


print(*arr)
np.stack


'''

### 3-02 조건 인덱싱(Boolean Indexing)
- Boolean Array의 값이 True값을 가지는 위치를 value Array에서 선택
   - Boolean Array가 Mask처럼 동작
- 조건 인덱싱의 결과는 항상 1차원 Array
- 배열에 조건 비교를 하는 경우 Element Wise(Broadcast) 연산으로 인해 각 요소별 비교 결과(True, False) 값을 가지게 됨
- 교재 그림 참조


'''

arr = np.arange(9).reshape(3, 3)
bidx = (arr % 2) == 0
print(bidx)
print(arr[bidx]) # boolean arr를 쓰면 2차원이더라도 1차원으로 나온다


arr = np.arange(27).reshape(3, 3, 3)
bidx = (arr%2) == 1

print(bidx)
print(arr[(arr%2) == 1])
# print(arr[(arr < 8) & (arr > 5)]) # 5초과인 인수, 8 미만


'''

팬시 인덱싱

'''
arr = np.arange(9).reshape(3, 3)
arr[2, 1:].reshape(1, 2)

print(arr[[0, 1], [1,1]]) # = [arr[0, 1], arr[1, 1]]

print([arr[0, 0], arr[1, 1], arr[2, 2]])
print(arr[0,:].size)
print([arr[i, i] for i in range(arr[0,:].size)])



'''

정수 인덱싱

'''
print("-----------------------------------------------------------")
arr = np.arange(9).reshape(3, 3)
print(arr[:2, 1:])

arr[2, 1:].reshape(1, 2)

print(arr[2:, 1:])
print(arr[2:, 1:].reshape(2,1)) # 갯수만 같아도 reshape 할 수 있음


print("-----------------------------------------------------------")
# shallow copy
b = arr[:, 1] # view : interface만 새롭게 만들고, 원본 데이터와 같은 메모리 참조

# deep copy
b = arr[:, 1].copy()

arr = np.arange(9).reshape(3, 3)


print(arr)
tmp = np.where(arr%2==0)
ridx, cidx = tmp
print(tmp)
print(ridx, cidx) 

print(arr[ridx, cidx], arr[arr%2 == 0]) # FANCY IDX, BOOLEAN IDX


arr = np.array([-1, 1, 0, -2, 3, -7])
# 0보다 작은 것을 0으로 변경
print(np.where(arr < 0, 0, arr))

'''

# var - 편차 제곱의 합, std - (평균 - 값 = 편차)
중요

'''
# var - 편차 제곱의 합, std - (평균 - 값 = 편차)
arr = np.array([160, 170, 180, 165, 172])
arr_mean = arr.mean()

# 분산
print(((arr_mean - arr)**2).sum()/len(arr), arr.var())

# 표준편차
print(arr.std(), np.sqrt(arr.var()))


print("------------------------------------------------------------")

arr = np.arange(9).reshape(3,3)

print(arr)
print(arr.sum(axis=None))
print(arr.sum(axis=0)) # axis는 방향을 의미 -> 행과 행을 연산, 연산의 방향이 행이 바뀌는 방향이다.
print(arr.sum(axis=1)) # 열과 열의 합 연산 결과를 반환
# axis는 진행 방향이고 음수도 존재한다.


