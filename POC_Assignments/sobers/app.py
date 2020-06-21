import os
import glob

from util.util import *

writeCSVfilename = 'output/merge.csv'
writeJSONfilename = 'output/merge.json'

def fileFinder(path, extention):
    all_files = glob.glob(os.path.join(path, extention))
    return all_files


def run_csv():
    os.remove(writeCSVfilename)
    for file in fileFinder("./data/","*.csv"):
        print('===' * 15)
        print('Processing file : ', file)
        print('===' * 15)
        obj = DataPreprocessor(CsvMerger(readfilename=file),
                               CsvMerger(writefilename=writeCSVfilename))
        obj.process()
        print('Processed to CSV')

def run_json():
    os.remove(writeJSONfilename)
    for file in fileFinder("./data/", "*.csv"):
        print('===' * 15)
        print('Processing file : ', file)
        print('===' * 15)
        obj = DataPreprocessor(JsonMerger(readfilename=file),
                          JsonMerger(writefilename=writeJSONfilename))
        obj.process()
        print('Processed to JSON')

if __name__ == '__main__':
    run_csv()
    run_json()