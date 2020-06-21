import os
import glob

from util.util import *

writeCSVfilename = 'output/merge.csv'
writeJSONfilename = 'output/merge.json'
writeXMLfilename = 'output/merge.xml'

def fileFinder(path, extention):
    all_files = glob.glob(os.path.join(path, extention))
    return all_files


def run_csv():
    if os.path.isfile(writeCSVfilename):
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
    if os.path.isfile(writeJSONfilename):
        os.remove(writeJSONfilename)
    for file in fileFinder("./data/", "*.csv"):
        print('===' * 15)
        print('Processing file : ', file)
        print('===' * 15)
        obj = DataPreprocessor(JsonMerger(readfilename=file),
                          JsonMerger(writefilename=writeJSONfilename))
        obj.process()
    print('Processed to JSON')

def run_xml():
    if os.path.isfile(writeXMLfilename):
        os.remove(writeXMLfilename)
    for file in fileFinder("./data/", "*.csv"):
        print('===' * 15)
        print('Processing file : ', file)
        print('===' * 15)
        obj = DataPreprocessor(XmlMerger(readfilename=file),
                               XmlMerger(writefilename=writeXMLfilename))
        obj.process()
    print('Processed to XML')



if __name__ == '__main__':
    run_csv()
    run_json()
    run_xml()