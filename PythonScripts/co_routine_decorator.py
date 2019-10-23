
#I've talked about the need to prime a coroutine by calling next on it or by sending a None value to it. I'll show you why
# that has to be done and an easy way to get around this. If we take a look at the counter function from the last video,
# this will start from the top and execute until it reaches the first yield. Until it has paused at yield, sending a value
# to the coroutine simply won't work. I'll open the shell and send a value to it before I have primed it so we can see the
# error again. This error is pretty descriptive of what I did wrong. It let's me know that I must either call next or send
# a None value so that the coroutine object has advanced to the point of being suspended at the yield point. Having to prime
# a coroutine seems a little hackey at best and it's easy to forget. An easy solution to this problem is a coroutine_decorator

# Coroutine_decorator is a function that is to be used as a decorator function. It takes a function as a parameter then it defines
# a new function within called wrap. Wrap will create a coroutine object and prime it by calling next and return that object. By
# simply including or importing this function into your code and using the coroutine_decorator before your actual coroutine function,
# it will cause your coroutine function to return a pre-primed coroutine object

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