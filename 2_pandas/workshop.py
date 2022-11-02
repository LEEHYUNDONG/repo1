import pandas as pd
import numpy as np
import seaborn as sns

# 0
np.random.seed(1234)
df = pd.DataFrame(np.random.randint(100,200,60).reshape(12, 5))
print(df)

# 1
df.columns = ['P01', 'P02', 'P03', 'P04', 'P05']
print(df)

# 2
#코드를 입력해 주세요
# index 생성 
# date_range 함수 이용 (주기는 월(M)으로 설정)
date = pd.date_range('20200101','20201231', freq='M')


date = pd.date_range('20200101','20201231', freq='D')
df = pd.DataFrame(np.random.randint(100, 200, 366*5).reshape(366, 5), index=date)
df.columns = ['P01', 'P02', 'P03', 'P04', 'P05']


print(df['20200401':'20200630'])

print(df.loc['20200531':'20200531', 'P01':'P03'])

df.loc['20200131':'20200131', :] = 0
print(df.loc['20200131':'20200131', :])

df['total'] = df[:].sum(axis=1)
print(df)

df['total rate'] = df['total']/5

print(df)

print(df.sort_values(by = 'total rate', ascending=True).head(3))


print(df.loc[df['total'] < 700])
df['state'] = ''

cond = (df['total'] >= 700)
df.loc[cond, 'state'] = 'Bad'
df.loc[~cond, 'state'] = 'Good'

print(df)