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

print(a.values)