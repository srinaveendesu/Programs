text = """****

***
 *

****

**
**

*
**
*
"""


def rotate(mat):
    m = len(mat) # rows
    n = len(mat[0]) # columns
    #print(mat)
    new_mat = []
    for _ in range(n):
        tmp = []
        for _ in range(m):
            tmp.append('0')
        new_mat.append(tmp)
    #new_mat = [['0'] * m] * n
    #print(new_mat)

    for c in range(n):
        for r in range(m):
            new_mat[c][r] = mat[m - 1 - r][c]
    #print(new_mat)

    return new_mat

def second_rotate(mat):
    m = len(mat) # rows
    n = len(mat[0]) # columns
    #print(mat)
    new_mat = []
    for _ in range(n):
        tmp = []
        for _ in range(m):
            tmp.append('0')
        new_mat.append(tmp)
    #new_mat = [['0'] * m] * n
    #print(new_mat)

    for c in range(n):
        for r in range(m):
            new_mat[c][r] = mat[r][c]
    #print(new_mat)

    return new_mat

def build_matrix(block):
    lst = []
    n = -100
    for row in block:
        #print(row, len(row), n)
        if len(row)> n:
            n= len(row)
    #print(n)
    for row in block:
        tmp = []
        for val in row:
            tmp.append(val)
        if len(tmp) != n:
            tmp.extend([' '] * (n - len(tmp)))
        lst.append(tmp)
    return lst


def fetchblock(text):
    lst = []
    text = text.split('\n')
    tmp_lst = []

    for val in text:
        if val == '':
            #print(build_matrix(tmp_lst))
            lst.append(tmp_lst)
            tmp_lst = []
            #print('huaha')
        else:
            tmp_lst.append(val)
    kst = []

    for l in lst:
        kst.append(build_matrix(l))
    #print(lst)
    #print(kst)
    return kst


def build_shape_matrices(text):
    first_mat = fetchblock(text)
    second_mat = []
    third_mat = []
    fourth_mat = []

    for val in first_mat:
        second_mat.append(rotate(val))

    for val in second_mat:
        third_mat.append(rotate(val))

    for val in third_mat:
        fourth_mat.append(rotate(val))

    return first_mat, second_mat, third_mat, fourth_mat


def convert_tuo_tuples(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = tuple(mat[i][j])
        mat[i] = tuple(mat[i])
    return mat


def find_unique(text):
    first_mat, second_mat, third_mat, fourth_mat = build_shape_matrices(text)
    first = convert_tuo_tuples(first_mat)
    second = convert_tuo_tuples(second_mat)
    third = convert_tuo_tuples(third_mat)
    fourth = convert_tuo_tuples(fourth_mat)
    final_dict = dict()
    for a,b,c,d,e in zip(first,second, third, fourth, range(len(first))):
        final_dict[a] = e
        final_dict[b] = e
        final_dict[c] = e
        final_dict[d] = e

    return len(set(final_dict.values()))


text2 = """****

***
 *

****

**
**

*
**
*

*
*
**

***
*
"""

text3 = """****

***
 *

****

**
**

*
**
*

*
*
**

***
*

**

*
*

***
*
***

* *
* *
***

 *
*  *
*  *
****

***
*  *
*
***

***
*  *
*
***

***
*
*  *
***
"""


"""
Assumptions
1. The last lego is followed by a newline
2. Only valid spaces are allowed for depicting the block.
If any unnecessary space is added, the program will break. 
For example:
***  |  *   | *   |  *
 *   | ***  | **  | **
            | *   |  *
A    |  B   | C   |  D
All the above blocks are same and each block is 
having a space only if needed for block definition.
For block A , in line 224 only 1 space given before "*".
For block B , in line 223 only 1 space given before "*".
For block C , in line 223,225 NO space is given after "*".
For block D , in line 223,225 1 space is given before "*". 
"""

print(find_unique(text))
print(find_unique(text2))
print(find_unique(text3))

"""
OUTPUT
3
4
8
"""
