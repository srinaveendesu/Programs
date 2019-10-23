
def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return wrap


@coroutine_decorator
def coroutine_example():
    while True:
        x = yield
        #do something with x
        print (x)


c = coroutine_example()

# as we can see we are not doing any priming of coroutine as the decorator is doing the same for us
c.send('sucess')

# sucess