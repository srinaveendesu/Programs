# Creating singleton functions
# The decorator makes sure that we always
# have only one instance of function

import functools

def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass


first_one = TheOne()
another_one = TheOne()

print (id(first_one))
print (id(another_one))

print(first_one is another_one)

# 4416392080
# 4416392080
# True