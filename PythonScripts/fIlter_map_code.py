"""
Now that we’ve got our generators, iterators, and iterables out of the way, we can start with some fun built-in functions.

Let’s start with `filter()`.

The `filter()` function is a built-in function in Python that you can call from any file or program.

It takes two arguments:

* A function; and
* An iterable (now we know what these are!)

It goes like this:
"""

friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(lambda x: x.startswith('R'), friends)
print(start_with_r)  # generator!
# <filter object at 0x10848b690>

print(list(start_with_r))
print(list(start_with_r))  # won't work, the generator has already gone through all its elements

# ['Rolf', 'Randy']
# []

"""
The function, which is the first argument, must return `True` or `False`. It must also have one parameter which is the current element of the list we’re working with.

The list we’re working with is the second argument to the `filter()` function.

The `filter()` function then returns a generator of the elements for which the first argument returns `True`.

Basically, using the `filter()` function is identical to this generator expression:
"""

(friend for friend in friends if friend.startswith('R'))

"""
Which is pretty much identical to this function:
"""

def my_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i

"""
> Why would you use `filter()`?

If you are only working in Python and with Python developers: you wouldn’t.

However, few languages have list and generator comprehensions like the expression above. If you are working with developers familiar with constructs like `filter()`, `map()`, and `reduce()`, which are popular in other languages, it could be beneficial to use them instead.

In the further reading section of this lecture I link you to a StackOverflow answer that has a lot more reading on when you could use which.
"""


###########################################################
###########################################################
###########################################################
###########################################################

"""
The `map()` function is used to take an iterable and output a new iterable where each element has been modified according to some function.

For example, this `map()`:
"""

friends = ['Rolf', 'Charlie', 'Anna']
friends_lower = map(lambda x: x.lower(), friends)

print(friends_lower)
# <map object at 0x10848b9d0>

print(list(friends_lower))
# ['rolf', 'charlie', 'anna']

"""
This of course could be written (arguably better / more pythonically) as a list or generator comprehension:
"""

friends_lower = [friend.lower() for friend in friends]

friends_lower = (friend.lower() for friend in friends)

"""
However there is something to be said for using `map()` and *not* creating the useless `friend` variable that you need to create for list comprehension.

I still think list comprehension is more pythonic and more readable.

However, if you already have the function you’re going to use defined, `map()` may not be such bad a choice. Here’s an example:
"""

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


# imagine these users are coming from a database...

users = [
    { 'username': 'rolf', 'password': '123' },
    { 'username': 'tecladoisawesome', 'password': 'youaretoo' }
]

user_objects = map(User.from_dict, users)

"""
The option of using a list comprehension is slightly uglier, I feel:
"""

user_objects = [User.from_dict(u) for u in users]

"""
Although of course, using dictionary unpacking everything would be made much simpler… More on that in a coming section!
"""