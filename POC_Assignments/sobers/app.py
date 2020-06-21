#import util.util as u

from util.util import *
import sys
import pandas as pd
import numpy as np

#print('ss', dir(CsvMerger))

#obj = CsvMerger(open('data/bank1.csv'),open('data/merger.csv','w+'))
obj = DataPreprocessor(CsvMerger(readfilename='data/bank1.csv'),CsvMerger(writefilename='output/merge_test.csv'))
obj.process()


import os
import glob
import pandas as pd

path = "./data/"
all_files = glob.glob(os.path.join(path, "*.csv"))

print(all_files)
# print('==='* 30)
# pd.options.display.float_format = "{:,.2f}".format
# df = pd.read_csv('data/bank3.csv',parse_dates=True,header=0)
# print(type(df))
# df = df.apply(lambda col: pd.to_datetime(col, errors='ignore')
#               if col.dtypes == object
#               else col,
#               axis=0)
#
#
# print('\n',df)
# print(df.dtypes)
# print(df.columns)
#
# columns = ['from','to']
# for col in df.select_dtypes(include=['datetime','object']):
#     print(col)
#     columns.insert(0,col)
#
# #print(df.columns[found].str.split("."))
# print(columns,df.columns)
#
# print(df[columns])
#
# df2 = df[df.columns.difference(columns,sort= False)]
# merge_colums = list(df2.columns)
# print(df2)
# print(merge_colums)
# try:
#     df2['amount'] = df2[merge_colums[0]].map(str) + '.' + df2[merge_colums[1]].map(str)
#     df2['amount'] =df2['amount'].astype(float)
#     df2['amount'] =df2['amount'].round(decimals=2)
#
#     print(df2)
# except:
#     pass
# try:
#     df3 = pd.concat([df[columns],df2['amount']],axis=1).reindex(df.index)
# except:
#     df3 = pd.concat([df[columns], df2[list(df2.columns)[0]]], axis=1).reindex(df.index)
# df3 = df3.rename({list(df.select_dtypes(include=['object']))[0]: 'transaction'},axis='columns')
# df3 = df3.rename({list(df.select_dtypes(include=['datetime']))[0]: 'date'},axis='columns')
#
# print(list(df.select_dtypes(include=['object']))[0])
# print(df3)
# print(df3.dtypes)
# df3.round(2)
#
# #df3.to_csv('data/file_name.csv', index=False)
#
# import os
# # if file does not exist write header
# if not os.path.isfile('data/file_name.csv'):
#    df3.to_csv('data/file_name.csv',index=False)
# else: # else it exists so append without writing the header
#    df3.to_csv('data/file_name.csv', mode='a', header=False,index=False)