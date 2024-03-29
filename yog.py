
# Day 1
x = lambda a,b : a*b
print (x(2,3))

# list comprehension

# dictionary comprehension - day 4
a = ['a','b','c']
d = {a[i] : i+1 for i in range(0,len(a))}
print (d)
d = {a[i] +'aa' : i+1 for i in range(0,len(a))}
print (d)
d = {a[i] *3 : i+1 if i >5 else 99 for i in range(0,len(a))}
print(d)

d = {'a':1, 'b':2, 'c':3, 'd':4}
print({i:('even' if j%2 == 0  else 'odd') for i,j in d.items()})



# sets
# Items in a set may be of different types, but they must be hashable
# Instances of type set are mutable, and thus, not hashable;
# instances of type frozenset are immutable and hashable.
# You can’t have a set whose items are sets,
# but you can have a set (or frozenset) whose items are frozensets.
# Sets and frozensets are not ordered.
print(type( {i for i in range(0,10)}    ))

print(  (i for i in range(0,10))    ) # to create a generator


# Creating iterators and generators
# Must implement
# __next__() -> The __next__() method must return the next item in the sequence.
# __iter__()  -> The __iter__() method returns the iterator object itself.
# and raise StopIteration when no values found

# Iterabale
# An object is called iterable if we can get an iterator from it . THe iter() function gives an iterator from them.
# It can be looped over. It returns an iterator object from dunder __iter__ method

# Iterator is an object which can remember its state during iteration. it is done by implementing
# __next__ method on the iterator object

# iterable -> __iter__
# iterator -> __Iter__ and __next__

# Often, for pragmatic reasons, iterable classes will implement both __iter__() and __next__() in the same class,
# and have __iter__() return self, which makes the class both an iterable and its own iterator. It is perfectly
# fine to return a different object as the iterator, though.

#generators

# a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
# It is as easy as defining a normal function with yield statement instead of a return statement.
# StopIteration is automatically raised

class gen:
    def __init__(self,limit):
        self.value = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >self.limit:
            raise StopIteration
        self.value = self.value +1
        return self.value

d = gen(10)
print(type(d))
print(next(d))
ss =iter(gen(10))
print(type(ss))
print(next(ss))

def s():
    i = 0
    for i in range(0,12):
        yield i
d = s()


print(type(d))
print(next(d))


#filter functions

lst = [1,2,3,4,5,6,7,8,9]
def func(val):
    if val%2:
        return False
    else:
        return True


print(list(filter(func,lst)))

# shallow copy/Deep Copy
# importing copy module
import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]

# using copy for shallow copy
# Copy using '=' operator also is shallow copying
li2 = copy.copy(li1)

# using deepcopy for deepcopy
li3 = copy.deepcopy(li1)

#A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
#A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.


# DECORATOR
def outer(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner

@outer
def test(*args,**kwargs):
    return 'this is decorated func ' + ' '.join(args) + ' '.join(kwargs.keys())

print(test())
print(test('a','b','c'))
print(test(a1='1',a2='2',a3='3'))

#======================================================
def big_outer(*dargs,**dkwargs):
    def outer(func):
        def inner(*args,**kwargs):
            return func(*args,**kwargs)
        return inner
    print('this is in decor ' + ' '.join(dargs) + ' '.join(dkwargs.keys()))
    return outer

@big_outer()
def test1(*args,**kwargs):
    return 'this is main func ' + ' '.join(args) + ' '.join(kwargs.keys())

@big_outer('aa','bb','cc',aa1='1',aa2='2',aa3='3')
def test2(*args,**kwargs):
    return 'this is main func ' + ' '.join(args) + ' '.join(kwargs.keys())

print(test1())
print(test1('a','b','c'))
print(test1(a1='1',a2='2',a3='3'))


print(test2())
print(test2(aa1='1',aa2='2',aa3='3'))

#CLASS DECORATOR
class decor:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):

        return self.func(*args, **kwargs)

@decor
def test(*args, **kwargs):
    return 'this is test func ' + ' '.join(args) + ' '.join(kwargs.keys())

print(test())
print(test('a',a1=1))
#======================================================
class decor:
    def __init__(self,*dargs,**dkwargs):
        self.dargs = dargs
        self.dkwargs = dkwargs

    def __call__(self, func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        print('this is the call class ' + ' '.join(self.dargs) + ' '.join(self.dkwargs.keys()))
        return inner

@decor()
def test(*args, **kwargs):
    return 'this is test func ' + ' '.join(args) + ' '.join(kwargs.keys())

@decor('c',c1=1)
def test1(*args, **kwargs):
    return 'this is test func ' + ' '.join(args) + ' '.join(kwargs.keys())

print(test())
print(test('a',a1=1))

######### integer and 'is' operator
# [-5,256] the address of variable is same.
a = 1
b=1
print (a is b)
# returns true

S1 = 'spam'
S2 = 'spam'
print(S1 == S2, S1 is S2)
(True, True)


S1 = 'a longer string'
S2 = 'a longer string'
print(S1 == S2, S1 is S2)
(True, False)




# context manager
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('trail.txt') as f:
    f.write('hello')

# context 2

from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with managed_file('hello.txt') as f:
     f.write('hello, world!')


# Python execution steps
#
# source code into format known as byte code
# byte code ( platform independent representation of source code)Python byte code is not binary machine code (e.g., instructions for an Intel or ARM chip).
# Byte code is a Python-specific representation.
# byte code can be run much more quickly then original source code statements
#
# if python has write access on machine Before 3.2 python create .pyc in same dir. after 3.2 __Pychache__ dir
# if it cannot write the byte code files to machine, the byte code is generated in memory and simply discarded on program exit.
# byte code is saved in files only for files that are imported, not for the top-level files of a program that are only run as scripts
#
# Once your program has been compiled to byte code (or the byte code has been loaded from existing .pyc files), it is
# shipped off for execution to PVM Python Virutal machine.it’s not a separate program, and it need not be installed by
# itself. In fact, the PVM is just a big code loop that iterates through your byte code instructions, one by one,
# to carry out their operations. The PVM is the runtime engine of Python; it’s always present as part of the Python system,
# and it’s the component that truly runs your scripts.
#
# Python’s traditional runtime execution model: source code you type is translated to byte code, which is then run by the Python Virtual Machine.
# Your code is automatically compiled, but then it is interpreted.
#
# frozen binaries
#
# Frozen binaries bundle together the byte code of your program files, along with the PVM (interpreter) and
# any Python support files your program needs, into a single package

# shebang #!

ord('A')
# 65
ord('Z')
# 90

ord('a')
# 97
ord('z')
# 122

chr(97)
# 'a'
chr(122)
# 'z'

int('1101', 2)             # Convert binary to integer: built-in
# 13

bin(13)                    # Convert integer to binary: built-in
# 0b1101

#   Python 3.0 and 2.6 introduced a new string type known as bytearray, which is
# mutable and so may be changed in place. bytearray objects aren’t really text
# strings; they’re sequences of small, 8-bit integers

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


#               Best     Average    Worst       Space
# Bubble Sort	Ω(n)	 θ(n^2)	    O(n^2)      1


def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

                # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

#                   Best     Average    Worst       Space
# Selection Sort	Ω(n^2)	 θ(n^2)	    O(n^2)      1


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#                   Best     Average    Worst       Space
# Insertion Sort	Ω(n)	 θ(n^2) 	O(n^2)      1



# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot



def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver code to test above

#                   Best              Average           Worst       Space
# Quick Sort	    Ω(n log(n))	      θ(n log(n))	    O(n^2)      O(log n)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),

#                   Best              Average           Worst       Space
# Quick Sort	    Ω(n log(n))	      θ(n log(n))	    O(n^2)      O(log n)


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

#                   Best              Average           Worst           Space
# Merge Sort	    Ω(n log(n))	      θ(n log(n))	    O(n log(n))     O(n)


# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    # Driver code to test above


arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print (arr)

#                   Best              Average           Worst           Space
# Heap Sort	        Ω(n log(n))	      θ(n log(n))   	O(n log(n))     o(1)


# using bucket sort
def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def bucketSort(x):
    arr = []
    slot_num = 10  # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

    # Put array elements in different buckets
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x


# Driver Code
x = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(x))
# k is number of buckets
#                   Best              Average           Worst           Space
# Bucket Sort	    Ω(n+k)	          θ(n+k)	        O(n^2)          o(n)


# Counting sort in Python programming


def countingSort(array):
    n = len(array)
    output = [0] * n

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, n):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = n - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, n):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)

# https://www.programiz.com/dsa/counting-sort
#                   Best              Average           Worst           Space
# Counting Sort	    Ω(n+k)	          θ(n+k)	        O(n+k)          o(k)

# A function to do counting sort of arr[] according to
# the digit represented by exp.
def radixcountingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] // exp1) %10
        count[index] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1) % 10
        output[count[index ] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

    # Method to do Radix Sort


def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        radixcountingSort(arr, exp)
        exp *= 10


# Driver code to test above
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
print(arr)

#                   Best              Average           Worst           Space
# Radix Sort	    Ω(nk)	          θ(nk)	            O(nk)           o(n+k)



# Namedtuple

from collections import namedtuple                     # Import extension type
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])       # Make a generated classbob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])        # A named-tuple record

bob = Rec(name='Bob', age=40.5, jobs=['dev', 'mgr'])

print (bob[0], bob[2])                                         # Access by position
#('Bob', ['dev', 'mgr'])
print (bob.name, bob.jobs)                                     # Access by attribute
#('Bob', ['dev', 'mgr'])
d = bob._asdict()                                      # Dictionary-like form
print (d['name'], d['jobs'])                                   # Access by key too
#('Bob', ['dev', 'mgr'])
print (d)


# PICKLE MODULE

D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
import pickle
pickle.dump(D, F)                          # Pickle any object to file
F.close()


F = open('datafile.pkl', 'rb')
E = pickle.load(F)                         # Load any object from file
E
#{'a': 1, 'b': 2}

#The pickle module is a more advanced tool that allows us to
# store almost any Python object in a file directly,
#The pickle module performs what is known as object
# serialization—converting objects to and from strings of
# bytes—but requires very little work on our part.

#shelve is a tool that uses pickle to store Python objects
# in an access-by-key filesystem,

#Notice that I opened the file used to store the pickled object in
# binary mode; binary mode is always required in Python 3.X, because
# the pickler creates and uses a bytes string object, and these
# objects imply binary-mode files


# JSON MODULE
name = dict(first='Bob', last='Smith')
rec  = dict(name=name, job=['dev', 'mgr'], age=40.5)
print (rec)

import json
json.dumps(rec)
#'{"job": ["dev", "mgr"], "name": {"last": "Smith", "first": "Bob"}, "age": 40.5}'
S = json.dumps(rec)
print(S)
#'{"job": ["dev", "mgr"], "name": {"last": "Smith", "first": "Bob"}, "age": 40.5}'
O = json.loads(S)
print(O)
#{'job': ['dev', 'mgr'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5}
print(O == rec)
# true
json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
print(open('testjson.txt').read())
# {
#     "job": [
#         "dev",
#         "mgr"
#     ],
#     "name": {
#         "last": "Smith",
#         "first": "Bob"
#     },
#     "age": 40.5
# }
P = json.load(open('testjson.txt'))
print(P)
#{'job': ['dev', 'mgr'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5}


# Struct MODULE

#the struct module knows how to both compose and parse packed binary data.
# In a sense, this is another data-conversion tool that interprets strings
# in files as binary data.



F = open('data.bin', 'wb')                     # Open binary output file
import struct
data = struct.pack('>i4sh', 7, b'spam', 8)     # Make packed binary data
print(data)
#b'\x00\x00\x00\x07spam\x00\x08'
F.write(data)                                  # Write byte string
F.close()

#The format string used here means pack as a 4-byte integer, a 4-character string
# (which must be a bytes string as of Python 3.2), and a 2-byte integer, all in big-endian form

F = open('data.bin', 'rb')
data = F.read()                                # Get packed binary data
print(data)
#b'\x00\x00\x00\x07spam\x00\x08'
values = struct.unpack('>i4sh', data)          # Convert to Python objects
print(values)
#(7, b'spam', 8)


# elipsses
# use of (...)

# zip
# 1) can have n arguments
# 2) prarallel traverse through sequences
# 3) zip truncates result tuples at the length of the shortest sequence when the argument lengths differ.

# Enumerate
lst = [1,2,3,4]

for i,k in enumerate(lst):
    print(i,k)

# LEGB Rule

# Python’s name-resolution scheme is sometimes called the LEGB rule, after the scope names:
# When you use an unqualified name inside a function, Python searches up to four scopes—the
# local (L) scope, then the local scopes of any enclosing (E) defs and lambdas, then the
# global (G) scope, and then the built-in (B) scope—and stops at the first place the name is
# found. If the name is not found during this search, Python reports an error.

# The global statement and its nonlocal 3.X cousin are the only things that are remotely like
# declaration statements in Python. They are not type or size declarations, though; they are namespace declarations.


#Non Local

# Like global, nonlocal declares that a name will be changed in an enclosing scope. Unlike global,
# though, nonlocal applies to a name in an enclosing function’s scope, not the global module scope
# outside all defs. Also unlike global, nonlocal names must already exist in the enclosing function’s
# scope when declared—they can exist only in enclosing functions and cannot be created by a first assignment in a nested def.
# nonlocal both    allows assignment to names in enclosing function scopes and limits scope lookups for such names to enclosing defs
# nonlocal names can appear only in enclosing defs, not in the module’s global scope or built-in scopes outside the defs

def tester(start):
    state = start  # Each call gets its own state

    def nested(label):
        nonlocal state  # Remembers state in enclosing scope
        print(label, state)
        state += 1  # Allowed to change it if nonlocal

    return nested

F = tester(0)
F('spam')  # Increments state on each call
F('ham')
print(F.state)
# spam 0
# ham 1
# AttributeError: 'function' object has no attribute 'state'

# 3.X, if we declare state in the tester scope as nonlocal within nested, we get to change it
# inside the nested function, too. This works even though tester has returned and exited by
# the time we call the returned nested function through the name F

# nonlocal restricts the scope lookup to just enclosing defs; nonlocals are not looked up in the
# enclosing module’s global scope or the built-in scope outside all defs, even if they are already there
# Python must resolve nonlocals at function creation time, not function call time.

# the nonlocal statement allows multiple copies of changeable state to be retained in memory. It
# addresses simple state-retention needs where classes may not be warranted    and global variables
# do not apply, though function attributes can often    serve similar roles more portably

def tester(start):
    def nested(label):
        print(label, nested.state)  # nested is in enclosing scope
        nested.state += 1  # Change attr, not nested itself

    nested.state = start  # Initial state after func defined
    return nested

F = tester(10)
F('spam')  # Increments state on each call
F('ham')

G = tester(42)
G('spam')  # Increments state on each call
G('ham')
print(G.state)

# spam 10
# ham 11
# spam 42
# ham 43
# 44


# function calls
# Function Arguments that must be passed by keyword only in calls (3.X)
def func(*other, name):
    pass

# Function Arguments that must be passed by keyword only in calls (3.X)
value = 10
def func(*, name=value):
    pass

# forcing a function to take keyword arguments
def kwonly(a, *b, c):
    print(a, b, c)

kwonly(1, 2, c=3)
#1 (2, ) 3
kwonly(a=1, c=3)
#1 () 3
kwonly(1, 2, 3)
#TypeError: kwonly() missing 1 required keyword - only argument: 'c'


def kwonly(a, *, b, c):
    print(a, b, c)

kwonly(1, c=3, b=2)
kwonly(c=3, b=2, a=1)
#1 2 3
#1 2 3
kwonly(1, 2, 3)
# TypeError: kwonly() takes 1 positional argument but 3 were given
kwonly(1)
# TypeError: kwonly() missing 2 required keyword-only arguments: 'b' and 'c'


def kwonly(a, *, b='spam', c='ham'):
    print(a, b, c)

kwonly(1)
kwonly(1, c=3)
kwonly(a=1)
kwonly(c=3, b=2, a=1)
kwonly(1, 2)
# 1 spam ham
# 1 spam 3
# 1 spam ham
# 1 2 3
# TypeError: kwonly() takes 1 positional argument but 2 were given


# Runtime operations that perform three distinct steps the first time a program imports a given file:
# Find the module’s file.
# Compile it to byte code (if needed). =>  During an import operation Python checks
#       both file modification times and the byte code’s Python version number to decide how to proceed.
# Run the module’s code to build the objects it defines.

# Bear in mind that all three of these steps are carried out only the first time a
# module is imported during a program’s execution; later imports of the same module
# in a program run bypass all of these steps and simply fetch the already loaded module object in memory

# compilation happens when a file is being imported. Because of this, you will not usually see a .pyc byte code file
# for the top-level file of your program, unless it is also imported elsewhere—only imported files leave behind .pyc
# files on your machine. The byte code of top-level files is used internally and discarded;
# byte code of imported files is saved in files to speed future imports.

# In Python 3.X, the from ...* statement form described here can be used only at the top
# level of a module file, not within a function. Python 2.X allows it to be used within a function,
# but issues a warning anyhow.

# When you call reload, Python rereads the module file’s source code and reruns its top-level statements.
# Perhaps the most important thing to know about reload is that it changes a module object
# in place; it does not delete and re-create the module object. Because of that, every reference to an entire module
# object anywhere in your program is automatically affected by a reload.

# reload runs a module file’s new code in the module’s current namespace.
# Top-level assignments in the file replace names with new values.
# Reloads impact all clients that use import to fetch modules
# Reloads impact future from clients only
# Reloads apply to a single module only

while i<4:  # Loop test
    i+=1
    pass  # Loop body
else:  # Optional else
    pass  # Run if didn't exit loop with break

for target in object:                 # Assign object items to target
    pass                        # Repeated loop body: use target
else:                                 # Optional else part
    pass                        # If we didn't hit a 'break'


# Package initialization
# The first time a Python program imports through a directory, it automatically runs all the code in the directory’s __init__.py file.
#
# Module usability declarations
# Package __init__.py files are also partly present to declare that a directory is a Python package.
#
# Module namespace initialization
# In the package import model, the directory paths in your script become real nested object paths after an import.

# you can use __all__ lists in __init__.py files to define what is exported when a directory is
# imported with the from * statement form. In an __init__.py file, the __all__ list is taken to be
# the list of submodule names that should be automatically imported when from * is used on the package
# (directory) name. If __all__ is not set, the from * statement does not automatically load submodules
# nested in the directory; instead, it loads just names defined by assignments in the directory’s __init__.py file,
# including any submodules explicitly imported by code in this file.


# As a special case, you can prefix names with a single underscore (e.g., _X) to prevent them from
# being copied out when a client imports a module’s names with a from * statement.
# Underscores aren’t “private” declarations: you can still see and change such names with other import
# forms, such as the import statement:


# # unders.py
# a, _b, c, _d = 1, 2, 3, 4
#
# >> > from unders import *  # Load non _X names only
# >> > a, c
# (1, 3)
# >> > _b
# NameError: name
# '_b' is not defined
#
# >> > import unders  # But other importers get every name
# >> > unders._b
# 2

# __all__    identifies names to be copied, while _X identifies names not to be copied.

# # alls.py
# __all__ = ['a', '_c']  # __all__ has precedence over _X
# a, b, _c, _d = 1, 2, 3, 4
# >> > from alls import *  # Load __all__ names only
# >> > a, _c
# (1, 3)
# >> > b
# NameError: name
# 'b' is not defined
# >> > from alls import a, b, _c, _d  # But other importers get every name
# >> > a, b, _c, _d
# (1, 2, 3, 4)
# >> > import alls
# >> > alls.a, alls.b, alls._c, alls._d
# (1, 2, 3, 4)

# dunder methods

# each module has a built-in attribute called __name__, which Python creates and assigns automatically as follows
# If the file is being run as a top-level program file, __name__ is set to the string "__main__" when it starts.
# If the file is being imported instead, __name__ is set to the module’s name as known by its clients.


# the __dict__ attribute is the namespace dictionary for most class-based objects

# inheritance search on attribute fetches, each instance has a link to its class that Python creates for us—it’s called __class__,
# >>> x.__class__                       # Instance to class link
# <class '__main__.rec'>

# Classes also have a __bases__ attribute, which is a tuple of references to their superclass objects
# rec.__bases__                     # Class to superclasses link, () in 2.X
# (<class 'object'>,)
#
# These two attributes are how class trees are literally represented in memory by Python


# __str__ for user-friendly displays and a __repr__ with extra details for developers to view. Because printing runs
# __str__ and the interactive prompt echoes results with __repr__,
# using __str__ instead limits a display’s scope, but leaves clients the option of adding a
# __repr__ for a secondary display at interactive prompts and nested appearances



# 1. Creational Design Patterns in Python
# 1.1. Abstract Factory Pattern
# 1.2. Builder Pattern
# 1.3. Factory Method Pattern
# 1.4. Prototype Pattern
# 1.5. Singleton Pattern
#
# 2. Structural Design Patterns in Python
# 2.1. Adapter Pattern
# 2.2. Bridge Pattern
# 2.3. Composite Pattern
# 2.4. Decorator Pattern
# 2.5. Façade Pattern
# 2.6. Flyweight Pattern
# 2.7. Proxy Pattern
# 2.8. MVC -Model view controller
#
# 3. Behavioral Design Patterns in Python
# 3.1. Chain of Responsibility Pattern
# 3.2. Command Pattern
# 3.3. Interpreter Pattern
# 3.4. Iterator Pattern
# 3.5. Mediator Pattern
# 3.6. Memento Pattern
# 3.7. Observer Pattern
# 3.8. State Pattern
# 3.9. Strategy Pattern
# 3.10. Template Method Pattern
# 3.11. Visitor Pattern


# CLASS CONCEPTS

# class’s method can always be called either through an instance (the usual way, where Python sends the instance to the
# self argument automatically) or through the class (the less common scheme, where you must pass the instance manually)

# instance.method(args...)
# class.method(instance, args...)

# Python uses inheritance to look for and call only one __init__ method at construction time—the lowest
# one in the class tree

# Python locates and calls just one __init__. If subclass constructors need to guarantee that superclass
# construction-time logic runs, too, they generally must call the superclass’s __init__ method
# explicitly through the class:

class Person:
    def __init__(self,name, job, pay):
        self.name =name
        self.job = job
        self.pay = pay

class Manager(Person):
    def __init__(self, name, pay):                     # Redefine constructor
        Person.__init__(self, name, 'mgr', pay)        # Run original with 'mgr'

# The built-in instance.__class__ attribute provides a link from an instance to the class from which it was created.
# Classes in turn have a __name__, just like modules, and a __bases__ sequence that provides access to superclasses.


# The built-in object.__dict__ attribute provides a dictionary with one key/value pair for every attribute attached
# to a namespace object (including modules, classes, and instances

# Inherited class attributes are attached to the class only, not copied down to instances

# All the statements inside the class statement run when the class statement itself runs
# Assignments to instance attributes create or change the names in the instance, rather than in the shared class.



# Psuedo private class attributes

# Two underscores at the front of the method name only: __gatherAttrs for us. Python automatically expands such names
# to include the enclosing class’s name, which makes them truly unique when looked up by the inheritance search.
# This is a feature usually called pseudoprivate class attributes,

# Abstract classes

# the superclass in this example is what is sometimes called an abstract superclass—a class that expects parts of its
# behavior to be provided by its subclasses. If an expected method is not defined in a subclass, Python raises an
# undefined name exception when the inheritance search fails.


class Super:
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError('action must be defined!')

X = Super()
X.delegate()
# NotImplementedError: action must be defined!

class Sub(Super): pass

X = Sub()
X.delegate()
# NotImplementedError: action must be defined!

class Sub(Super):
    def action(self): print('spam')

X = Sub()
X.delegate()
# spam


# As of Python 2.6 and 3.0, the prior section’s abstract superclasses (a.k.a. “abstract base classes”), which require
# methods to be filled in by subclasses, may also be implemented with special class syntax.

from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    @abstractmethod
    def method(self, *args):
        pass

# But in Python 2.6 and 2.7, we use a class attribute instead:

class Super:
    __metaclass__ = ABCMeta
    @abstractmethod
    def method(self, *args):
        pass

# Dunder methods 2

# instance creation first triggers the __new__ method, which creates and returns the new instance object,
# which is then passed into __init__ for initialization.

# If defined in a class (or inherited by it), the __getitem__ method is called automatically for instance-indexing
# operations. __getitem__ is also called for slice expressions—always in 3.X, and conditionally in 2.X
# L[slice(2, 4)]

# __getitem__ also turns out to be one way to overload iteration in Python—if this method is defined, for loops call
# the class’s __getitem__ each time through, with successively higher offsets.
# Python 2.X only, classes can also define __getslice__ and __setslice__ methods to intercept slice fetches and
# assignments specifically.

# __index__ method in Python 3.X for index interception—this method returns an integer value for an instance when
# needed and is used by built-ins that convert to digit strings

# generator functions and expressions, as well as built-ins like map and zip, proved to be single-iterator objects,
# thus supporting a single active scan. By contrast, the range built-in, and other built-in types like lists, support
# multiple active iterators with independent positions.

# classes may code a __contains__ method—when present, this method is preferred over __iter__, which is preferred
# over __getitem__. the specific __contains__ intercepts membership, the general __iter__ catches other iteration
# contexts such that __next__ (whether explicitly coded or implied by yield) is called repeatedly, and __getitem__
# is never called:


# The __getattr__ method intercepts attribute references. It’s called with the attribute name as a string whenever
# you try to qualify an instance with an undefined (nonexistent) attribute name. It is not called if Python can
# find the attribute using its inheritance tree search procedure.

# the __setattr__ intercepts all attribute assignments. If this method is defined or inherited,
# self.attr = value becomes self.__setattr__('attr', value).

# __delattr__, is passed the attribute name string and invoked on all attribute deletions

#
# Python calls __radd__ only when the object on the right side of the + is your class instance, but the object on the
# left is not an instance of your class.

# >>> x + 1                      # __add__: instance + noninstance
# add 88 1
# 89
# >>> 1 + y                      # __radd__: noninstance + instance
# radd 99 1
# 100
# >>> x + y                      # __add__: instance + instance, triggers __radd__
# add 88 <commuter.Commuter1 object at 0x00000000029B39E8>
# radd 99 88
# 187


# the destructor method __del__, is run automatically when an instance’s
# space is being reclaimed (i.e., at “garbage collection” time):



class Employer:
    Bonus = 0

    def __init__(self, firstname, pay):
        self.firstname = firstname
        self.pay = pay

    @classmethod
    def increment(cls, bonus):
        cls.Bonus = cls.Bonus + (bonus * 0.01)


    def payment(self):
        return round(self.pay * (1 + self.Bonus))

    @staticmethod
    def email(name):
        return f'{name}@domain.com'
    
class Manager(Employer):
    def __init__(self, name, pay):
        super().__init__(name, pay)
        

class Engineer(Employer):
    def __init__(self, name, pay):
        super().__init__(name, pay)

E1 = Employer('srinav', 50000)
E2 = Employer('jackryan', 60000)

print(f'Employer payment with bonus {E1.Bonus}: ', E1.payment())
print(f'Employer payment with bonus {E2.Bonus}:', E2.payment())

Employer.increment(5)

print(f'Employer payment after increment with bonus {E2.Bonus}:', E1.payment())
print(f'Employer payment after increment with bonus {E2.Bonus}:', E2.payment())

M = Manager('manager', 100000)

print(f'Manager payment with bonus {M.Bonus}: ', M.payment())

Manager.increment(5)

print(f'Manager payment after increment with bonus {M.Bonus}: ', M.payment())


En = Engineer('engineer', 80000)

print(f'Engineer payment with bonus {En.Bonus}: ', En.payment())

Engineer.increment(2)

print(f'Engineer payment after increment with bonus {En.Bonus} : ', En.payment())

print(M.email(M.firstname))


# Employer payment with bonus 0:  50000
# Employer payment with bonus 0: 60000
# Employer payment after increment with bonus 0.05: 52500
# Employer payment after increment with bonus 0.05: 63000
# Manager payment with bonus 0.05:  105000
# Manager payment after increment with bonus 0.1:  110000
# Engineer payment with bonus 0.05:  84000
# Engineer payment after increment with bonus 0.07 :  85600
# manager@domain.com

print(isinstance(1,int))
print(issubclass(Engineer, Employer))

# generator send

# eval() , exec()

# collections module

# manacher algorithm
# Floyd’s Cycle-Finding Algorithm
