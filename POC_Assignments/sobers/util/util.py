import os
import pandas as pd
from pandas.core.dtypes.generic import ABCDataFrame

__all__ = ['CsvMerger','JsonMerger','XmlMerger','DataPreprocessor']

class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        data = self.reader.read()
        if isinstance(data, ABCDataFrame):
            if len(data) ==0: return
        else:
            if not data: return
        if isinstance(data, ABCDataFrame):
            data = self.converter_dataframe(data)
        else:
            data = self.converter(data)
        self.writer.write(data)

    def converter(self, data):
        raise NotImplementedError('converter must be defined!')

    def converter_dataframe(self, data):
        raise NotImplementedError('converter must be defined!')

class DataPreprocessor(Processor):

    def converter(self, data):
        return data

    def converter_dataframe(self, dataFrame):
        df = dataFrame.apply(lambda col: pd.to_datetime(col, errors='ignore') if col.dtypes == object else col, axis=0)
        columns = ['from', 'to']
        for col in df.select_dtypes(include=['datetime', 'object']):
            columns.insert(0, col)
        df2 = df[df.columns.difference(columns, sort=False)]
        merge_colums = list(df2.columns)
        try:
            if len(merge_colums)>1:
                df2['amount'] = df2[merge_colums[0]].map(str) + '.' + df2[merge_colums[1]].map(str)
                df2['amount'] = df2['amount'].astype(float)
            else:
                df2['amount'] = df2[merge_colums[0]]
        except:
            pass
        try:
            df3 = pd.concat([df[columns], df2['amount']], axis=1).reindex(df.index)
        except:
            df3 = pd.concat([df[columns], df2[list(df2.columns)[0]]], axis=1).reindex(df.index)
        df3 = df3.rename({list(df.select_dtypes(include=['object']))[0]: 'transaction'}, axis='columns')
        df3 = df3.rename({list(df.select_dtypes(include=['datetime']))[0]: 'date'}, axis='columns')
        return df3


class CsvMerger():
    def __init__(self,readfilename=None,writefilename=None):
        self.readfilename = readfilename
        self.writefilename = writefilename

    def read(self):
        self.dataframe = pd.read_csv(self.readfilename, parse_dates=True, header=0)
        return self.dataframe

    def write(self,dataframe):
        if not os.path.isfile(self.writefilename):
            dataframe.to_csv(self.writefilename, index=False)
        else:  # else it exists so append without writing the header
            dataframe.to_csv(self.writefilename, mode='a', header=False, index=False)

class JsonMerger():
    def __init__(self,readfilename=None,writefilename=None):
        self.readfilename = readfilename
        self.writefilename = writefilename

    def read(self):
        self.dataframe = pd.read_csv(self.readfilename, parse_dates=True, header=0)
        return self.dataframe

    def write(self,dataframe):
        if not os.path.isfile(self.writefilename):
            dataframe.to_json(self.writefilename, orient='records')
        else:  # else it exists so append without writing the header
            df = pd.read_json(self.writefilename)
            dfout = pd.concat([dataframe,df])
            dfout.to_json(self.writefilename, orient='records')

class XmlMerger():
    pass


class PrivateExc(Exception):
    pass