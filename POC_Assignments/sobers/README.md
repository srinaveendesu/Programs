# Running Application

`cd sobers`

`python3 app.py`

# Running Unit Test:

`python3 -m unittest tests/sobers_test.py`

# **Extendability**

With a unified structure of  `DataPreprocessor()` ,

it can be used to extend/implement the required `converter()` that pre-processes csv files into appropriate 
required format. 

The `*Merger()` class can be used to implement the corresponding load/unload methods 
based on formats like csv, json, xml etc.


# OUTPUT

The csv and json output files are generated in `output` folder.


**Note: Assumptions made**

_1. All data files are in `data` folder_

_2. There will max of 6 coloumns and minimum of 5 columns_

_3. Every bank record will have following mandatory fields which are date, transaction, to, from  and money(euro/euro,cents) columns_

_4. The column names **TO** and **from** and datatype of columns in point 3 will not change_

_5. The column names for date type and transaction(string type ) can change_

_6. When monetary columns are in the form of euro and cents, cents if always followed by euro collumn_ 
