import numpy as np
import pandas as pd
import seaborn as sns

tipdf = sns.load_dataset('tips')
print(tipdf)


print(tipdf.ndim)

print(tipdf.shape)

print(tipdf.tail(3))

print(tipdf.info())


print(tipdf.sort_values(by='tip', ascending=False).head(3))

tipdf['tip_rate'] = tipdf['tip']/tipdf['total_bill']
print(tipdf)