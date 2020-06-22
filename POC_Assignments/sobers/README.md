# Running Application

`cd sobers`

`python3 app.py`

# Running Unit Test:

`python3 -W ignore -m unittest tests/sobers_test.py`

Run log

Processing csv data file

Processing csv data file and appending to output data file

Processing csv data file with coloumn names (d,transact,rupees,from,to)

Processing csv data file with coloumn names (timestamp,type,dollar,cents,from,to)

Processing csv data file with coloumn names (day,type,dollar,cents,from,to)

Processing csv data file with coloumn names (day,type,dollar,cents,to,from)

Processing csv data file with coloumn names (day,type,usd,cents,to,from)

Processing csv data file with 100000+ rows

0:00:01.222016
..
----------------------------------------------------------------------
Ran 2 tests in 1.370s

OK


# **Extendability**

The designed solution is generic, which provides a unified structure to meet all the business requirements and can also be reused/extended 
to different formats such as json, xml , sql, html etc   

With the unified structure of `DataPreprocessor` class, it provides a reader,a writer and a converter methods.

Reader    -> Extract data

converter -> Transform data

write     -> Loads data

The class can be used to extend/implement the required `converter()` method that pre-processes csv files and 
merges all files to a unified dataframe. 

The `*Merger` class can be used to implement the corresponding extract/load methods 
to get different formatted outputs like csv, json, xml, sql etc.

As part of current implementation json and xml load processor have been implemented

# **Performance Report** 

Ran tests on 100000+ rows and processing time for same is ~1.18 seconds

Run log


`python3 -W ignore -m unittest tests/sobers_test.py`

`...(truncated output)`

`Processing csv data file with 100000+ rows`

`Processed time 0:00:01.182847`

`...(truncated output)`

# OUTPUT

The **CSV ,JSON** and **XML** output files are generated in `output` folder.


**Note: Assumptions made**

_1. All data files are in `data` folder_

_2. There will max of 6 coloumns and minimum of 5 columns_

_3. Every bank record will have following mandatory fields which are 
**date**, **transaction**, **to**, **from**  and **money**(euro or euro,cents) columns_

_4. The column names **TO** and **from** and datatype of columns in point 3 will not change_

_5. The column names for date type and transaction(string type ) can change_

_6. When monetary columns are in the form of euro and cents, cents if always followed by euro collumn_ 
