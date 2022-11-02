import numpy as np
import pandas as pd



'''

dataframe

axis의 None은 0으로 인지한다.

'''
a = pd.DataFrame([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

print(a)

a.index = ['A', 'B', 'C']
a.columns = ['X1', 'X2', 'X3']

print(a)

print(a.rename({'A':'a'}, axis = 0))

a = a.rename(index={'A':'a'}, columns={'X1':'Y'})

print(a)

print(a.values, a.dtypes)


'''

dataframe column값 지정할 수 있음


'''

df = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6],
                   [7,8,9]],
                   columns=list('가나다'),
                   index=list('ABC')
                   )

df.columns.name = 'Cols'
# df.index.name = 'Rows'

print(df)



data = {
    'name':['Kim', 'Lee', 'Park'],
    'age' :[1, 2, 3],
    'children':[2, 0, 3]
}

df = pd.DataFrame(data)

print(df)

'''

하나의 컬럼만 가져오면 series가 됨.

df['name'] -> series

DataFrame에 key 값으로 column의 이름을 지정하여 column을 선택할 수 있습니다.
1개의 column을 가져올 수 있으며, **1개의 column 선택시 Series**가 됩니다.

(참고) column에 대해 label을 이용해 boolean array, slice를 사용하기 위해서는 df.loc[]을 사용해야함
- basic indexing 에서는 제공하지 않음

'''

print(df[['name', 'age']]) # 목록


dummy = {
    'food': ['KFC', 'McDonald', 'SchoolFood'],
    'price': [1000, 2000, 2500],
    'rating' : [4.5, 3.9, 4.2]
}
df = pd.DataFrame(dummy)
print(df)
print(df[['food', 'rating']])
df = df.rename({'food':'place'}, axis=1)
print(df)