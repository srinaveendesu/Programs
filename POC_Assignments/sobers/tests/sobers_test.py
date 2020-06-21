import os
import sys
import logging

import unittest
from util.util import *

logger = logging.getLogger()
logger.level = logging.DEBUG

class MyTestCase(unittest.TestCase):

    def test_dataprocessor(self):
        fread = open('./tests/test1.csv')
        fwrite = open('./tests/testOutput.csv','w')
        t = DataPreprocessor(fread,fwrite)
        t.process()
        fread.close()
        fwrite.close()
        with open('./tests/testOutput.csv') as f:
            data = f.read()
        os.remove('./tests/testOutput.csv')
        self.assertEqual(len(data), 0)

    def test_csvprocessor(self):
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        # Test1 :
        # Processing csv data file
        logging.getLogger().info('Processing csv data file')
        t = DataPreprocessor(CsvMerger(readfilename='./tests/test2.csv'),
                               CsvMerger(writefilename='./tests/testOutput.csv'))
        t.process()
        with open('./tests/testOutput.csv') as f:
            data = f.readlines()
        self.assertEqual(len(data), 3)

        # Test2 :
        # Processing csv data file and appending to output data file
        logging.getLogger().info('Processing csv data file and appending to output data file')
        t = DataPreprocessor(CsvMerger(readfilename='./tests/test3.csv'),
                             CsvMerger(writefilename='./tests/testOutput.csv'))
        t.process()
        with open('./tests/testOutput.csv') as f:
            data = f.readlines()
        os.remove('./tests/testOutput.csv')
        self.assertEqual(len(data), 5)

        # Test3 :
        # Processing csv data file with coloumn names (d,transact,rupees,from,to)
        logging.getLogger().info('Processing csv data file with coloumn names (d,transact,rupees,from,to)')
        t = DataPreprocessor(CsvMerger(readfilename='./tests/test4.csv'),
                             CsvMerger(writefilename='./tests/testOutput.csv'))
        t.process()
        with open('./tests/testOutput.csv') as f:
            data = f.readlines()

        self.assertEqual(len(data), 3)

        # Test4 :
        # Processing csv data file with coloumn names (timestamp,type,dollar,cents,from,to)
        logging.getLogger().info('Processing csv data file with coloumn names (timestamp,type,dollar,cents,from,to)')
        t = DataPreprocessor(CsvMerger(readfilename='./tests/test5.csv'),
                             CsvMerger(writefilename='./tests/testOutput.csv'))
        t.process()
        with open('./tests/testOutput.csv') as f:
            data = f.readlines()

        os.remove('./tests/testOutput.csv')
        self.assertEqual(len(data), 5)

        # Test5 :
        # Processing csv data file with coloumn names (day,type,dollar,cents,from,to)
        logging.getLogger().info('Processing csv data file with coloumn names (day,type,dollar,cents,from,to)')
        t = DataPreprocessor(CsvMerger(readfilename='./tests/test6.csv'),
                             CsvMerger(writefilename='./tests/testOutput.csv'))
        t.process()
        with open('./tests/testOutput.csv') as f:
            data = f.readlines()
        os.remove('./tests/testOutput.csv')
        self.assertEqual(len(data), 3)

        # Test6 :
        # Processing csv data file with coloumn names (day,type,dollar,cents,to,from)
        logging.getLogger().info('Processing csv data file with coloumn names (day,type,dollar,cents,to,from)')
        t = DataPreprocessor(CsvMerger(readfilename='./tests/test7.csv'),
                             CsvMerger(writefilename='./tests/testOutput.csv'))
        t.process()
        with open('./tests/testOutput.csv') as f:
            data = f.readlines()
        os.remove('./tests/testOutput.csv')
        self.assertEqual(len(data), 3)

        # Test7 :
        # Processing csv data file with coloumn names (day,type,usd,cents,to,from)
        logging.getLogger().info('Processing csv data file with coloumn names (day,type,usd,cents,to,from)')
        t = DataPreprocessor(CsvMerger(readfilename='./tests/test8.csv'),
                             CsvMerger(writefilename='./tests/testOutput.csv'))
        t.process()
        with open('./tests/testOutput.csv') as f:
            data = f.readlines()

        os.remove('./tests/testOutput.csv')
        self.assertEqual(len(data), 3)

        # Test8 :
        # Processing csv data file with 100000+ rows
        import datetime
        logging.getLogger().info('Processing csv data file with 100000+ rows')
        start = datetime.datetime.now()
        t = DataPreprocessor(CsvMerger(readfilename='./tests/test.csv'),
                             CsvMerger(writefilename='./tests/testOutput.csv'))
        t.process()
        end = datetime.datetime.now()
        print('Processed time ',end - start)
        with open('./tests/testOutput.csv') as f:
            data = f.readlines()

        os.remove('./tests/testOutput.csv')
        self.assertEqual(len(data), 131681)


if __name__ == '__main__':
    unittest.main()
