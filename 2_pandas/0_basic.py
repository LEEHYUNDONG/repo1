import pandas as pd
import numpy as np

'''

pandas 버전 알아보기

'''
print(pd.__version__)


'''

pandas series 이용하기

'''

arr = pd.Series([1, 5, 10, -4])
print(arr)

arr = pd.Series(['부장', '차장', '짜장', '차두리'])
print(arr)

'''

series를 만들때 series나 1d ndarray를 사용하면
copy되지 않고, 동일한 데이터를 참조 (view)
그러나, 이런 개념을 사용하지 말자, copy 개념을 사용하자
아래의 pd.Series에 dtype='int32'를 넣으면, copy=False라고 해도, copy-True로 동작함
왜?? arr의 dtype이 'int64'이기 때문에, 물리적으로 달라서 view가 안됨

'''

arr = np.arange(100, 105)

s = pd.Series(arr, dtype='int32', index=list('ABCDE'), name='number', copy=False)

arr[0] = 0
print(arr)
print(s.values)
print(type(s.values))


a= pd.Series(np.arange(50.0, 55.0, 1), dtype='float32')
print(a)

a = pd.Series(['apple', np.nan, 'banana', 'kiwi', 'gubong'], index=list('가나다라마'))
print(a)
k = list('가나다라마')
v = ['apple', np.nan, 'banana', 'kiwi', 'gubong']
data = dict(zip(k, v))
print(data)


'''

series index
loc - 일반 인덱스
iloc - 설정한 인덱스

[]만 있으면 basic 인덱스이다

(label) index가 integer일 때

**fancy indexing**은 index를 선택하여 list로 정의하고, 선택한 index list로 indexing 하는 방법입니다.

**boolean index**은 index list 에서 **True인 index 만 선택**합니다.
주의해야할 점은 반드시 boolean index list의 갯수와 Series의 갯수가 맞아야 합니다.

'''

s = pd.Series(['손흥민', '김연아', '봉준호', '이현동'], index=[i for i in range(1, 5)])
print(s)

print(s.iloc[-1])


print(s.loc[1], s.iloc[1]) # loc은 내가 지정한 인덱스, iloc은 암묵적으로 제공하는 인덱스 -> label

a = np.arange(12)
a = a.reshape(3, 4)
print(a.shape)

a = np.reshape(a=a, newshape=(3, 4))


s = pd.Series(['손흥민', '김연아', '봉준호', '이현동', np.nan], index=[i for i in range(1, 6)])

print(s.isnull())
print(s[s.isna() != 1])

print(s.isna().sum())
# 결측치 비율
print(s.isna().mean()*100)


print(s.notnull())

'''

label index는 시작과 끝을 모두 포함함 ex) a['a':'c']
integer index는 끝을 포함하지 않음

'''

