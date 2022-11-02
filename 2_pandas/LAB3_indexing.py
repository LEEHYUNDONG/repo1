'''

데이터 분석

'''

import numpy as np
import pandas as pd
import seaborn as sns
from mySUNI import cds
from IPython.display import Image

df = sns.load_dataset('titanic')
print(df.head())


import shelve

# titanic data 저장
with shelve.open('data\\cj1031_data') as data:
    data['titanic'] = df
    print('Done')

print(df.head(10))

# 생존확률이 높은 사람
# pclass =3 alone = False, 

print(df.groupby('pclass')[['survived']].mean())
print(df.groupby('alone')[['survived']].mean())
print(df.groupby('parch')[['survived']].mean())

print(df.groupby('adult_male')[['survived']].mean())
print(df.groupby('embark_town')[['survived']].mean())
print(df.groupby('embark_town')[['fare']].mean())

A = df.loc[df['fare']>= 50, 'survived'].mean()
B = df.loc[df['fare'] < 50, 'survived'].mean()

print(A, B)

print(df.groupby(['pclass', 'sex'])[['survived']].mean())


'''

**object** 타입은 쉽게 문자열이라고 생각하면 됩니다.

그런데, **category** 타입도 있습니다. category 타입은 문자열이지만, 
'남자' / '여자'처럼 카테고리화 할 수 있는 컬럼을 의미 합니다. 나중에 별도로 다루겠습니다.

'''

print(df.describe())


'''

데이터 분석
1. 데이터셋 가져오기 - pd.read_xxx()
2. 데이터셋의 정상 여부 - df.head(), df.tail()
3. 행, 열, 결측치 여부, 데이터 타입, 메모리 사용량 - df.info()
4. df.describe()



'''

'''
# 연속형 데이터
# ex) 키 : 160, 170, 몸무게, 기온, 판매량, 가격, 

# 1 2 3 4 -> 등간격이면 수치형 <-> 간격이 동일하지 않으면 서열형

# 범주형 데이터
# 성별(0-남, 1-여), 메달, 혈액형
## 명목형 :성별, 혈액형
## 서열형 (순서형) : 메달

'''


# 범주형 - value_counts()

print(df['who'].value_counts())

# 비율
print(df['who'].value_counts(normalize=True))

who = df['who'].value_counts()
who.plot.pie()

'''

데이터 분석에서 행의 수는 열의 수보다 적어도 10배 이상이어야 한다

'''
# 항구에 따른 비율
print(df['embark_town'].value_counts())
print(df.index, df.columns)
print(df.values) # ndarray

'''

결측치에 타입 변환은 필수적임

'''

print(df['pclass'].astype('int32').head(5))

s = pd.Series([123, 456, 789])
s2 = s.astype('str')
s3 = s.astype('object')

print(s, s2, s3)

print([type(x) for x in s2])

print([type(x) for x in s3])

'''

category
- 주어진 category 이외의 다른 값을 사용하지 못함
- 메모리 절약
- 문자열에 대한 숫자값 구하기 (label encoding)


'''
# s = df['pclass'].astype('category').copy()
# s[0] = 4 # 불가

s = pd.Series(['여자', '남자', '아이'] * 10).to_frame()
s.info(memory_usage='deep')