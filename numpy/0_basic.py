import numpy as np

a = np.array([1, 2, 3, 4])
print(a)

'''
1000 1004 1008 1012 1016 1020
1   2   3   4   5   6

interface(배열 정보를 가지고 있는 저장소)
시작주소 :0x1000
ndim - 2
shape - (2, 3)
size - 6
dtype - int32
stride - (12, 4)

차원을 구분해서 공부하라

## 이부분이 가장 헷갈리는데 잘 구분해놓는 것이 좋음 ##

interface(배열 정보를 가지고 있는 저장소)
시작주소 :0x1000
ndim - 1
shape - (6,)
size - 6
dtype - int32
stride - (24, 4)

'''

# 기본 numpy attr 출력하고 이용하기
A = np.array([1, 2, 3, 4])
print(A.ndim, A.shape, A.size, A.strides, a.dtype)

A = np.array(10)
print(A.ndim, A.shape)

def displayNPAttr(a):
    print(a)
    print(f'ndim :{a.ndim}, shape: {a.shape}, size: {a.size}, dtype: {a.dtype}, strides : {a.strides}')
    

A = np.array([1, 2, 3, 4])
displayNPAttr(A)

B = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

displayNPAttr(B)

C = np.array([
    [
        [0, 1, 2, 3],
        [0, 1, 2, 3],
        [0, 1, 5, 3],
    ]
])

displayNPAttr(C)

print("--------------------------------------------------------------------------------------")
tmp = np.array(range(10))
print(tmp)
tmp = np.arange(10)
print(tmp)

np.linspace

print("--------------------------------------------------------------------------------------")

A = np.eye(5, dtype='int32')
print(A)

'''
용어는 전부다 외워야 한다.
array 차원, 차원별 크기
총 개수
데이터 유형 
### 1-02 Numpy Array 속성
- ndim : ndarray의 차원을 나타냄
- shape : 각 차원의 ndarray 크기를 튜플 형태로 나타냄
- size : ndarray에있는 요소의 총 수
- dtype : ndarray의데이터 유형
   - uint8 ~ uint64, int8 ~ int64, float16 ~ float128, bool 등
- T : ndarray의 전치된 결과 반환 (행열 바꾸기)

### 1-03 Numpy 배열 형태 변경
- Numpy Array의 가장 큰 장점은 형태(shape)를 자유자재로 변경 가능
- 단, 변경 전 데이터 개수와 변경 후 데이터의 개수(size)는 같아야 함
- Numpy Array의 형태를 바꾸기 위해서는 reshape 함수를 이용
- -1은 딱 1번만 사용 할 수 있으며 자동으로 적절한 형태를 계산


'''


# reshape

arr = np.arange(16)
print(arr, arr.shape)
arr2 = arr.reshape(4, 4)
print(arr2, arr2.shape)

# print(np.sctypeDict)


x = np.array([[1,2], [3,4]])
y = np.array([[5,6], [7,8]])

print(np.add(x, y))

'''
scalar 연산은 broadcasting 덕에 자동으로 할 수 있음
'''

print(x+1)

'''
## 3.Numpy Indexing (중요)

- Index는 행렬, 배열, 리스트 등에서 특정 요소를 빠르게 참조할 수 있음
- 별도의 수단으로 일반적으로 정수 값을 사용하며 정수는 특정 요소의 위치(순서)를 의미함
- 파이썬의 시퀀스 자료형에서 사용한 것과 동일하게 대괄호([])를 사용하여 특정 요소에 접근이 가능함
- 기존 파이썬의 시퀀스 자료형에서는 차원에 따라 대괄호를 사용 했지만 Numpy 에서 대괄호는 한번만 사용됨
   - 예) 2차원 리스트에서 데이터 접근 : **list[0][1]**
   - 예) 2차원 Numpy Array에서 데이터 접근 : **array[0, 1]**
- Numpy의 경우 정수 인덱싱, 조건 인덱싱, 팬시(Fancy) 인덱싱을 지원함
'''

arr = np.arange(9).reshape(3, 3)
print(arr)

# 첫번쨰 행 출력 기왕이면 그래도 써주는게 좋다.
print(arr[0, :], arr[0])


# arr의 마지막 열 출력
print(arr[:, -1])

print("------------------------------------------------------------------------------------------------------")

arr = np.arange(36).reshape(2, 3, 3, 2)
print(arr)
