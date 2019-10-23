# I've mentioned already that it is possible for a single coroutine to both send and receive values.
# Similar to the pipelines I've showed you with generators earlier in the course, coroutines can also
# be used to create data pipelines. I've opened up 0305 router pipeline from the exercise files. In this
# file there are two coroutines called router and file_write. These are set up to work in line. I can send
# data initially to the router coroutine. The router coroutine is able to do something that generators are
# not able to do. It both receives data and sends it. The router coroutine can branch in more than one direction
# and send to multiple targets. This coroutine will take the lines from the names file, split it into first and
# last names, and then send each one to a different target. The two targets are simply separate instanciations
# of the file_write coroutine. Coroutines are able to do this because the whole process is being driven from the
# beginning. Data is being pushed through the pipeline, rather than pulled like it was with generator pipelines.
# Because of this, it can be sent off in different ways. And it doesn't rely on multiple end targets needing to
# pull the data through. What will happen is that the names file data will pass through this pipeline, which is
# the sender, the router and the file_write coroutines. And first names will go one direction, and printed in one
# file, while last names will be printed in a different file. At the bottom of the file, I've created the two file_
# write coroutine objects, and the router coroutine object. I've also include the logic to send all the data in the
# names.txt file into the router.send method, and closed the router.


def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return wrap


@coroutine_decorator
def router():
    try:
        while True:
            line = yield
            (first, last) = line.split(' ')
            fnames.send(first)
            lnames.send(last.strip())
    except GeneratorExit:
        fnames.close()
        lnames.close()


@coroutine_decorator
def file_write(filename):
    try:
        with open(filename, 'a') as file:
            while True:
                line = yield
                file.write(line + '\n')
    except GeneratorExit:
        file.close()
        print
        'one file created'


if __name__ == "__main__":
    fnames = file_write('first_names.txt')
    lnames = file_write('last_names.txt')
    router = router()
    for name in open('names.txt'):
        router.send(name)
    router.close()



# when the code is run the data being process will create two files one with first names
# and two with last names while reading the file on the fly