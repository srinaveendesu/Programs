#Coroutines are used to consume values, but they need a producer that will send it values to consume. And the initial producer
# is not going to be a coroutine. I've opened up Oh three, oh four slash use coroutine from the exercise files to show an example.
# The first function in the file is called sender. This function takes a file name and a target as parameters. This is just a regular
# function and is not a coroutine. Sender is what's going to be driving the action in this example. By hooking up a sender function with
# a coroutine object, I'm having the sender function read all the lines from a file that I pass in, and send the lines one by one to a
# coroutine. When it's done reading the file, it will automatically close the coroutine. The function match counter is going to be the
# target coroutine. And it will search for a particular string in every value sent to it. I'll open up a shell on the right side of the
# screen to give a demonstration of the process. I'll need a coroutine object to pass in as the target of the sender. So I'll call match
# counter and pass in Da as the text that it will search for, and the resulting coroutine object will be assigned to c. Then I'll call the
# sender function and pass in names.txt as the file that will search through and c as the coroutine object. This is the names.txt file that
# our sender function will look through line by line searching for the string Da. As you can see, it found five instances of Da in those names.
# The concept of coroutines has allowed me to keep the logic of opening and reading files completely separate from filtering and counting it.
# If I wanted to pass the data to a different coroutine that does something else with it, I can just pass a different target in. At the bottom
# of the used coroutine file, there's another function called longer than. It will print out items longer than (n) from the file it reads. I'll
# open up a shell again and we can see a demonstration of that. I'll call longer than, then I'll pass in (14) as the length of the string we're
# looking for. Now I'll call the same sender function and pass in names.txt again with this target. It printed out 23 names from that list that
# are longer than 14 characters. These separate functions that work together allow me to keep my logic separate and reusable. It will be easy to
# substitute a different target coroutine, different sender, or add other pieces.

def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return wrap

def sender(filename, target):
    for line in open(filename):
        target.send(line)
    target.close()


@coroutine_decorator
def match_counter(string):
    count = 0
    try:
        while True:
            line = yield
            if string in line:
                count += 1
    except GeneratorExit:
        print ('{}: {}'.format(string, count))


@coroutine_decorator
def longer_than(n):
    count = 0
    try:
        while True:
            line = yield
            if len(line) > n:
                print(line)
                count += 1
    except GeneratorExit:
        print('longer than {}: {}'.format(n, count))


c = match_counter('Da')
sender('names.txt',c)

# Da: 5

l = longer_than(15)
sender('names.txt',l)

# Armanda Pilling
#
# joLahoma Mondragon
#
# Calista Overbay
#
# Lashanda Demoura
#
# Bong Humbertson
#
# Vasiliki Stonge
#
# Danita Vallance
#
# Sergio Cockrill
#
# Delaine Creamer
#
# Tanesha Finkbeiner
#
# Leonore Cushman
#
# Alphonse Bellomy
#
# Deadra Bisceglia
#
# Josefine Montijo
#
# Brittanie Talamantes
#
# Octavio Trumbull
#
# longer than 15: 16