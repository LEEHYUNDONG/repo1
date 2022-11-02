'''

라이브러리 import 

'''
import numpy as np
import pandas as pd
from IPython.display import display, Image
from mySUNI import cds


# cds.list_data()
# cds.download_data(['서울시대중교통', '서울시주민등록인구', 'PandasFileIO'])

'''

excel 불러오기

- engine : excel문서의 입출력을 담당하는 라이브러리
- 별도의 설치가 필요
- xlsx : openpyxl을 사용함
- pandas에서 자동으로 engine 지정이 되지만 동작이 안되면 직접 지정할 것
xlsx engine = 'openpyxl

'''

import os

# filename = os.path.join('data', 'seoul_transportation.xlsx')

# print(filename)
# excel = pd.read_excel(filename)

# basic 인덱스 slice는 행에 대해서 동작한다.
# print(excel.head(5)) # 위 5개만 출력 = excel[:5]


# pd.set_option('display.max_rows', 1000)
# pd.set_option('display.max_columns', 200)

# print(excel)

# excel = pd.read_excel(filename, sheet_name='버스')
# print(excel)

# excel = pd.read_excel(filename, sheet_name=None)
# dic = dict(excel)
# print(dic.keys())
# print(dic['철도']) # sheet_name을 주는것과 같고 dataframe이 된다.

# print(dic['철도'].head(30))


# 엑셀 저장
# excel.to_excel('data\\sample.xlsx', index=True)


# 파일, 네트워크 등의 리소스를 사용하고, 반납하는 코드는 with statement를 사용한다.
# 별도의 반납은 작성할 필요가 없음

# with pd.ExcelWriter('data\\sample2.xlsx') as writer:
#     excel.to_excel(writer, index=False, sheet_name='샘플1')


# [add] 작업중인 객체를 저장하는 방법
# dictionary 형태의 데이터, rw를 함께 사용, binary file
# import shelve

# filename = os.path.join('data', 'seoul_transportation.xlsx')

# excel = pd.read_excel(filename, sheet_name=None)

# print(excel)

# with shelve.open('data\\cj1031_data') as data:
#     data['bus'] = excel['버스']
#     data['train'] = excel['철도']
    
# with shelve.open('data\\cj1031_data') as data:
#     lst = list(data['bus'])

# df = pd.read_excel('data\\mySUNI.xlsx', sheet_name= None)
# # df = pd.read_excel('data\\mySUNI.xlsx', sheet_name= ;2020년 07월)

# df.keys()
# df_07 = df['2020년 07월']
# df_07.to_excel('2020년 07월 서울 브랜드별 평균 휘발유 가격.xlsx', index=False)
# print(df_07)


'''

# csv - text file

- 한 줄이 한 개의 행에 해당하며, 열 사이에는** 쉼표(,)를 넣어 구분**합니다.
- Excel보다는 훨씬 가볍고 **차지하는 용량이 적기 때문에 대부분의 파일데이터는 csv 형태**로 제공됩니다.

(참고) 쉼표를 찍어 놓은 금액 데이터(100,000)를 CSV에 직접 집어넣으면 나중에 해석할
때 서로 다른 열로 취급되므로 문제가 될 수 있습니다. 
해결책으로 쉼표 대신 탭 문자(\t)를 구분자로 사용하는 것이다. 
이러한 경우 **Tab Separated Values(TSV)**라고 부른다.

'''


# df = pd.read_csv('data\\seoul_population.csv', encoding='utf-8')
# print(df.head(10))


########################################################

import os

def get_encoding(filename):
    import chardet
    with open(filename, 'rb') as fb:
        enc = chardet.detect(fb.readlines()[0])['encoding']
    return enc


# filename = os.path.join('data', 'seoul_population.csv')
# df = pd.read_csv(filename, encoding=get_encoding(filename), thousands=',')

# # df.to_csv('data\\test.csv', index=False, encoding='cp949')
# df.to_csv('data\\test.csv', index=False, encoding='utf-8')

# print(df)

# print(df.dtypes)
# print(df['인구 합계'].to_list())


# df = pd.read_csv('data\\seoul_population.csv', chunksize=10)
# print(df)



#####################################################################

# df = pd.read_csv('data\\mySUNI_1.csv', encoding=get_encoding('data\\mySUNI_1.csv'))
# print(df.head(2))
# df = pd.read_csv('data\\mySUNI_2.csv', encoding=get_encoding('data\\mySUNI_2.csv'))
# print(df.head(2))
# df = pd.read_csv('data\\mySUNI_3.csv', encoding=get_encoding('data\\mySUNI_3.csv'), sep='|')
# df = pd.read_csv('data\\mySUNI_3.csv', encoding=get_encoding('data\\mySUNI_3.csv'), sep='|', chunksize=5)
# print(df.read(4))

#####################################################################

import glob

fileNameLst = sorted(glob.glob('data\\*.csv'))
print(fileNameLst)

for filename in fileNameLst:
    try:
        df = pd.read_csv(filename, encoding=get_encoding(filename), sep=',')
        print(df.head(5))
    except:
        df = pd.read_csv(filename, encoding=get_encoding(filename), sep='|')
        print(df.read(5))
    