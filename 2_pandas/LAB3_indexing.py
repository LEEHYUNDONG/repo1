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

print(df.sort_values(by='pclass', ascending=True))
print(df.sort_values(by=['sibsp', 'parch'], ascending=[False, False]))


#######################################################################################

df = sns.load_dataset('titanic')


print(df.loc[2, 'age'])

print(df.loc[2 : 5, ['age', 'fare', 'who' ]])

print(df.loc[2 : 5, 'class':'deck'])

'''

boolean array를 쓰는경우에는 iloc은 안쓰는게 좋다.

'''

condition = (df['who'] == 'man')
condition2 = (df['age'] > 25)

print(df.loc[condition & condition2, :])


##############################

df = sns.load_dataset('titanic')

cond1 = (df['who'] == 'man')
cond2 = (df['age'] >= 30)
res = df.loc[cond1 & cond2, :].sort_values(by='fare', ascending=False).head(10)
print(res)

##############################

df = sns.load_dataset('titanic')

cond1 = ((df['pclass'] == 1) | (df['pclass'] == 2))
cond2 = ((df['age'] >= 20) & (df['age'] < 40))
res = df.loc[cond1 & cond2, ['survived', 'pclass', 'age', 'fare']].head(10)
print(res)


'''

## iloc
- `loc`와 유사하지만, integer index만 허용합니다.
- loc와 마찬가지고, indexing / slicing 모두 가능합니다.



'''


'''

## isin
특정 값의 포함 여부는 isin 함수를 통해 비교가 가능합니다. 
(파이썬의 in 키워드는 사용 불가 합니다.)


'''

sample = pd.DataFrame({'name': ['kim', 'lee', 'park', 'choi'], 
                        'age': [24, 27, 34, 19]
                      })
print(sample)

print(sample['name'].isin(['kim', 'lee']))

condition = sample['name'].isin(['kim', 'lee'])
print(sample.loc[condition])


'''

## where


`DataFrame.where(cond, other=nan, inplace=False, axis=None, level=None, errors='raise', try_cast=False)`

Pandas의 `where`는 Numpy의 `where`와 동작이 다릅니다.

- cond: True/False로 판단될 수 있는 식
- other: condition을 만족하지 못하는 요소에 할당 할 값

'''

print(df['fare'].where(df['fare']<20, 0))

# [add]  df.query()

print(df.query('age > 20 and age < 40 and pclass==3').head(10))